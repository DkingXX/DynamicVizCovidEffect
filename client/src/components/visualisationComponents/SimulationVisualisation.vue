<template>
  <div>
    <div v-if="loading">
      <!--<keep-alive>-->
      <LoadingScreen/>
      <!-- </keep-alive>-->
    </div>
    <d3-network v-else :class="getSimulationClass()" :net-nodes="nodes" :net-links="links" :options="options"/>

  </div>
</template>

<script>
import D3Network from "vue-d3-network";
import * as req from "../../helpers/request";
import {mapActions} from 'vuex'
import LoadingScreen from "@/components/generalUseComponents/LoadingScreen";

export default {

  name: "SimulationVisualisation",
  props: {simulation: Object, customSimulation: Object, readyCount: Number, useReady: Boolean},
  components: {
    D3Network, LoadingScreen
  },
  data() {
    return {
      refreshCoefficient: 1000, // refresh the data based on the refresh coefficient
      nodeSizeIncrement: 0.0075, // step for each increment
      // smaller init node size in comparison view since there are two networks in it
      globalNodeSize: this.$route.name !== 'Comparison' ? 15 : 12.5,
      // as there is no space for displaying node name in comparison view
      displayName: this.$route.name !== 'Comparison',
      loading: false,
      infectNr: 0,
      sourceData: [],
      active_idx: -1,
      snapshot: [],
      nodes: [],
      links: [],
      simStep: 20,
      nextPressed: false,
      snapshotIndex: 0,
      index: 0,
      options: {
        nodeSize: this.globalNodeSize,
        nodeLabels: true,
        linkWidth: 0.5,
        resizeListener: true,
        force: this.$route.name !== 'Comparison' ? 500 : 200,
      },
      timer_status: "stop",
      resetFlag: false,
      // tmp to start_mode
      tmp_start_mode: 0
    };
  },
  computed: {
    isEnd() {
      return this.active_idx >= this.sourceData.length - 1;
    },
  },
  watch: {
    // watch the #ready sims, when all are ready, run init_map to show the map
    readyCount(newVal) {
      if (newVal === 2) {
        this.loading = false
        this.init_map(this.simulation.simulationData.data.contents[this.tmp_start_mode])
      }
    }
  },
  methods: {
    ...mapActions(['resetSimulation']),
    getSimulationClass(){
      return this.$route.name !== 'Comparison' ? 'fit-parent-general-purpose ' : 'fit-parent ' + 'sim_negative'
    },
    // send msg to parent that init is done
    send_init_done() {
      this.$emit('getReady')
    },
    // get the data from the server and validate the request
    request_data(start_node) {
      let current = this
      console.log(this.simulation.simulationData.data)
      if (!this.simulation.simulationData.data.populated) {
        req.run_sim(this.simulation.dataset, this.simulation.blockProb / 100, this.simulation.recoveryRate / 100, this.simulation.seedNode, this.simulation.infectRate / 100, this.simulation.mode.toLowerCase(),
            function (err, body) {
              if (err) {
                console.log(err)
              } else {
                console.log('Simulation Data Received')
                // when the callback finishes store the data
                current.storeBody(body, start_node)
              }
            })
      } else {
        // if the data is already there, just run the simulation
        this.alert_init(start_node)
      }
    },
    storeBody(body, start_node) {
      // store the body into the state class
      // to access the simulation (by start node),
      // use the following line:  this.simulation.simulationData.data.contents[start_node]
      this.simulation.simulationData.data.contents[start_node] = JSON.parse(body);
      this.alert_init(start_node)
    },
    // alert when the simulation is received from the server and start to display the simulation
    alert_init(start_node) {
      // stop the loading screen
      // this.loading = false
      // the simulation data will be computed after the request is processed
      // this.simulation.simulationData.snapshotReady = false
      // this.init_map(this.simulation.simulationData.data.contents[start_node])

      this.simulation.simulationData.snapshotReady = false
      if (this.useReady) {
        // don't init_map directly, but tell the parent I'm ready
        this.tmp_start_mode = start_node
        this.send_init_done()
      } else {
        // directly run init_map to show the result
        this.loading = false
        this.init_map(this.simulation.simulationData.data.contents[start_node])
      }
    },
    init_map(json) {
      this.nodes.length = 0;
      this.links.length = 0;
      var nodes_count = json["nodes_count"];
      this.simulation.simulationData.statsInfo[2].value = nodes_count
      var seed_node = json["seed"];
      // add all nodes to array and mark them green as not infected except the seed node
      for (var i = 0; i <= nodes_count; i++) {
        let nodeName = "" + i
        // display the node name only when it is necessary
        if (this.displayName)
          nodeName += " " + json['names'][i]

        this.nodes.push({id: i, _color: "green", name: nodeName, _size: this.globalNodeSize});
      }
      this.infect = json["infect"];
      this.rec = json["rec"];
      this.contact = json["contact"];
      this.contact_num = this.contact.length;
      this.nodes[seed_node]._color = "red"; // seed node is infected at the beginning

      this.simulation.simulationData.maxProgress = this.contact.length
      this.infect_list = [];

      this.infect_list.push(seed_node) // push the infected one into the list

      this.rec_list = [];
      console.log(this);
      clearTimeout(this.timer);
      this.index = 0;

      // refresh the stats before the simulation starts
      this.refreshStats()

      // let speedBackup = this.simulation.simulationData.visualisationSpeed
      // this.simulation.simulationData.visualisationSpeed = 0
      this.infect_map();
      console.log(this.snapshot)
      // this.simulation.simulationData.visualisationSpeed = speedBackup
    },
    infect_map() {
      // stop the simulation if the reset button was pressed

      this.links.length = 0;
      for (let i = 0; i < this.simStep && this.simulation.simulationData.isRunning; i++) {

        // refresh the stats and plots
        this.refreshStats()
        // update the progress once every 150 contacts
        if (this.index % 150 === 0) {
          // refresh only if the rate increases
          if (this.logStats(this.infect_list.length))
            this.refreshPlots()
          this.simulation.simulationData.simulationProgress = this.index
        }
        if (this.index === this.contact_num) { // stop when all contacts are added
          this.simulation.simulationData.simulationProgress = this.index
          this.refreshPlots()
          // the snapshot was fully computed
          this.simulation.simulationData.snapshotReady = true;
          this.links = []
          return;
        }

        var source_node = this.contact[this.index][1];
        var target_node = this.contact[this.index][2];

        // increase their size based on how many contacts they had
        this.nodes[source_node]._size += this.nodeSizeIncrement
        this.nodes[target_node]._size += this.nodeSizeIncrement

        // deal with exceptions
        if (source_node < 0 || source_node > this.nodes_count || target_node < 0 || source_node > this.nodes_count) {
          console.log("error:" + source_node + "error:" + target_node)
        }
        if ( // if the target node is infected as read from the api, but local list doesn't mark it
            this.infect[this.index].includes(target_node) &&
            !this.infect_list.includes(target_node)
        ) {
          this.infect_list.push(target_node); // then mark it as infected.
          this.nodes[target_node]._color = "red";
          this.links.push({
            sid: this.nodes[source_node],
            tid: this.nodes[target_node],
            _color: "red",
          }); // mark current connection as infected as well
        } else if ( // if the source node is recovered from api but local list doesn't mark it
            this.rec[this.index].includes(source_node) &&
            !this.rec_list.includes(source_node)
        ) {
          this.rec_list.push(source_node); // mark it locally as recovered
          this.nodes[source_node]._color = "purple";
          this.links.push({
            sid: this.nodes[source_node],
            tid: this.nodes[target_node],
            _color: "green",
          }); // mark current connection as recovered
        } else {
          this.links.push({
            sid: this.nodes[source_node],
            tid: this.nodes[target_node],
            _color: "blue",
          }); // any else situations, mark current connection as normal
        }
        this.index = this.index + 1; // go to check the next connection
      }

      this.timer = setTimeout(() => {
        this.infect_map(this.index)
      }, this.simulation.simulationData.visualisationSpeed);

    },
    checkSim(start_node) {
      this.request_data(start_node)
    },
    stop() { // Pause the simulation
      this.simulation.simulationData.isRunning = false
      this.timer_status = "stop";
    },
    start() { // Start the simulation
      // this will allow the server to run smoothly
      // even if the user wants to see the computation for every node,
      // the data will be delivered one by one based on the start_node

      //check if the data is valid
      if (this.simulation.dataset === "") {
        alert("Please choose the dataset");
      } else if (this.simulation.mode === "") {
        alert("Please choose the mode");
      } else if (this.simulation.seedNode === '') {
        alert("Please choose the seed node");
      } else if (this.simulation.blockProb === 0) {
        alert("Please choose the Block Probability");
      } else if (this.simulation.infectRate === 0) {
        alert("Please choose the Infect Rate");
      } else if (this.simulation.recoveryRate === 0) {
        alert("Please choose the Recovery Rate");
      } else {

        if (!this.simulation.simulationData.isRunning) {
          // run the simulation
          // Use this if you don't want to use a high amount of memory
          // this.checkSim(0);
          // Or use this if you want to use a higher amount of memory but the data will be stored in the memory
          // this.checkSim(this.simulation.start_node)

          if (!this.simulation.simulationData.data.started) {
            this.checkSim(0)
            this.loading = true
            this.simulation.simulationData.data.started = true
          }
          this.simulation.simulationData.isRunning = true
        } else
          this.simulation.simulationData.isRunning = false
      }
    },
    next() { // go to the snapshot of the next graph
      console.log(this.index)
      if (this.index + this.simStep <= this.contact_num) {
        this.index = this.snapshot[this.snapshotIndex].index
        this.active_idx = this.snapshot[this.snapshotIndex].active_idx
        this.links = this.snapshot[this.snapshotIndex].links
        this.nodes = this.snapshot[this.snapshotIndex].nodes
        this.simulation.simulationData.simulationProgress = this.snapshot[this.snapshotIndex].progress
      }
    },
    refreshStats() {
      // get number of infected people for displaying on GUI
      this.simulation.simulationData.statsInfo[0].value = this.infect_list.length
      // get number of recovered people for displaying on GUI
      this.simulation.simulationData.statsInfo[1].value = this.rec_list.length
      // update statistics
    },
    logStats(value) {
      // see if something changed regarding the infection rate
      // if yes change the infectNr
      if (this.infectNr !== value) {
        this.infectNr = value
        return true;
      }
      return false;
    },
    refreshPlots() {
      // update the statistics for the plots
      this.$emit('updateStatistics')
    },
    saveSnapshot() { // The snap shot of the current graph will be saved
      // not used due to high memory use
      this.snapshotIndex++
      this.snapshot.push(
          JSON.parse(
              JSON.stringify({
                index: this.index,
                active_idx: this.active_idx,
                links: this.links,
                nodes: this.nodes,
                progress: this.simulation.simulationData.simulationProgress
              })
          )
      );
    },
    reset() { // Reset the simulation
      this.resetFlag = true;
      this.resetSimulation(this.simulation);
      this.stop();
      clearTimeout(this.timer);
      this.simulation.simulationData.data.started = false
      this.simulation.simulationData.isRunning = false
      this.simulation.simulationData.simulationProgress = 0
      this.simulation.simulationData.data.populated = false

      // stop the loading and reset the links and nodes
      this.loading = false
      this.nodes = [];
      this.links = [];

      // reset all parameters of 1st sim
      this.simulation.simulationData.statsInfo[0].value = 0
      this.simulation.simulationData.statsInfo[1].value = 0
      this.simulation.simulationData.statsInfo[2].value = 0

      // refresh the charts
      this.$emit('resetCharts')
    },
    getIndexAndStep(){ // for echart display
      return [this.index,this.simStep]
    }
  },
}
;
</script>
