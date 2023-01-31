<template>
  <div class="comparison-view">
    <NavigationBar/>
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-2">
          <StatsBar :statsInfo="this.simulations[simulationId].simulationData.statsInfo"
                    :customStatusInfo="this.customSimulation.simulationData.statsInfo"
                    :isReset="this.resetFlagForStatsBar"/>

        </div>
        <div class="col-md-8">
          <div class="row"> <!-- area for 2 networks graph -->
            <div class="col-md-6">

              <SimulationVisualisation :simulation="this.simulations[simulationId]"
                                       @getReady="this.handle_ready"
                                       :readyCount="this.count_init_done"
                                       :useReady="this.use_count"
                                       @updateStatistics="this.updateLine"
                                       @resetCharts="this.resetCharts"
                                       ref="simulationVisualisation"/>

            </div>
            <div class="col-md-6">

              <SimulationVisualisation :simulation="this.customSimulation"
                                       @getReady="this.handle_ready"
                                       :readyCount="this.count_init_done"
                                       :useReady="this.use_count"
                                       @updateStatistics="this.updateLine"
                                       @resetCharts="this.resetCharts"
                                       ref="customSimulationVisualisation"/>

            </div>

          </div>

          <eLine :series="infect_line_series"
                 :title="'Number of infected people over time'"/>

          <div class="row">

            <SimulationNavigationButtons :simulation="this.simulations[simulationId]"
                                         @start-sim="startSim"
                                         @stop-sim="stopSim"
                                         @reset-sim="resetSim"
            ></SimulationNavigationButtons>

          </div>
        </div>

        <div class="col-md-2">
          <AdvancedLeftView :use-comparison="true" :simulation="this.simulations[simulationId]"
                            :comparison-sim="customSimulation"/> <!-- panel for 1st sim -->
        </div>

      </div>

    </div>

  </div>

</template>


<script>
import SimulationVisualisation from "@/components/visualisationComponents/SimulationVisualisation";
import NavigationBar from "@/components/advancedViewComponents/NavigationBar";
import StatsBar from "@/components/advancedViewComponents/StatsBar";
import SimulationNavigationButtons from "@/components/advancedViewComponents/SimulationNavigationButtons";
import {mapState} from 'vuex'
import AdvancedLeftView from "@/components/advancedViewComponents/AdvancedLeftView";

export default {
  name: 'ComparisonView',
  components: {
    AdvancedLeftView, NavigationBar, SimulationVisualisation, SimulationNavigationButtons, StatsBar
  },
  data() {
    return {
      simulationId: this.$route.params.id,
      // the 2nd simulation object user defined
      customSimulation: {},
      // the flag indicates the status of reset(reset: true, not reset: false)
      // this flag is used to tell StatsBar.vue whether the mission has been reset or not
      resetFlagForStatsBar: false,
      // whether use counter of ready state
      use_count: true,
      // count amount of sv in ready state
      count_init_done: 0,
      //line index
      line_index: 1,
      // settings for infect curve
      infect_line_series: [
        {
          name: 'Left Simulation',
          type: 'line',
          minInterval: 250,
          smooth: 0.6,
          areaStyle: {},
          showAllSymbol: true,
          data: []
        },
        {
          name: 'Right Simulation',
          type: 'line',
          smooth: 0.6,
          minInterval: 250,
          areaStyle: {},
          showAllSymbol: true,
          data: []
        }
      ],
      // settings for recovered curve
      recovered_line_series: [{
        name: 'origin sim',
        type: 'category',
        showAllSymbol: true,
        data: []
      },
        {
          name: 'sim to be compared',
          type: 'category',
          showAllSymbol: true,
          data: []
        }]
    }
  },
  created() {
    this.customSimulation = this.deepCopy(this.simulationStructure)
  },
  watch: {
    count_init_done(newVal) {
      if (newVal > 2) this.count_init_done = 2
    }
  },
  computed: {
    ...mapState(['simulations', 'simulationStructure', 'modes'])
  },
  mounted() {
    this.resetCharts()
  },
  methods: {
    resetCharts() {
      // reset the data in each plot
      this.infect_line_series.forEach(element => element.data = []);
      this.recovered_line_series.forEach(element => element.data = []);
      this.count_init_done = 0
    },
    // get ready msg from SimulationVisualisation, then increment count_init_done to track #ready sims
    handle_ready() {
      this.count_init_done++
    },
    deepCopy(obj) {
      let copyObj = Array.isArray(obj) ? [] : {}
      for (let key in obj) {
        copyObj[key] = typeof (obj[key]) === "object" ? this.deepCopy(obj[key]) : obj[key]
      }
      return copyObj
    },
    // link the buttons with their implementation in the child (SimulationVisualisation)
    // the execution tree looks like this:
    // SimulationNavigationButtons - emits start event
    // Parent (this view) catches the event
    // Parent sends the event to the SimulationVisualisation component
    startSim() { // start the simulation
      this.resetFlagForStatsBar = false
      this.$refs.customSimulationVisualisation.start()
      this.$refs.simulationVisualisation.start()
    },
    stopCustom() { // pause customSimulation
      this.customSimulation.simulationData.isRunning = false
      this.$refs.customSimulationVisualisation.timer_status = "stop";
    },
    stopSim() { // stop the simulation
      this.$refs.simulationVisualisation.stop()
      this.stopCustom()
    },
    resetSim() { // reset the simulation
      // reset the number of ready sv
      this.count_init_done = 0

      this.resetFlagForStatsBar = true
      this.$refs.simulationVisualisation.reset()
      this.resetCustom()
    },
    resetCustom() { // reset the parameters of customSimulation
      this.$refs.customSimulationVisualisation.resetFlag = true
      this.customSimulation = this.deepCopy(this.simulationStructure)

      this.stopCustom()

      this.customSimulation.simulationData.data.started = false
      this.customSimulation.simulationData.isRunning = false
      this.customSimulation.simulationData.simulationProgress = 0
      this.customSimulation.simulationData.data.populated = false

      this.$refs.customSimulationVisualisation.loading = false
      this.$refs.customSimulationVisualisation.nodes = [];
      this.$refs.customSimulationVisualisation.links = [];

      // reset number of infected/recovered people & number of nodes to 0 of customSimulation
      this.customSimulation.simulationData.statsInfo[0].value = 0
      this.customSimulation.simulationData.statsInfo[1].value = 0
      this.customSimulation.simulationData.statsInfo[2].value = 0

      // if above code doesn't work, close following comment,
      // and copy following code with replacing
      // 'customSimulation' to 'simulation',
      // then take them to append the function SimulationVisualisation.vue/reset
      this.customSimulation.seedNode = ''
      this.customSimulation.blockProb = 0
      this.customSimulation.recoveryRate = 0
      this.customSimulation.infectRate = 0
      this.customSimulation.repeats = 0
      this.customSimulation.iterations = 0

    },
    // update curves, update every time the data is requested
    updateLine() {
      //let d = new Date()
      //let str = d.getHours()+':'+d.getMinutes()+':'+d.getSeconds()

      // index as x-axis - first comments for more accurate data
      //let refData = this.$refs.customSimulationVisualisation.getIndexAndStep()
      //let timestamp = Math.round(refData[0] / refData[1]).toString()

      // this lien for smoother plots
      let timestamp = this.line_index.toString()
      this.line_index++
      // get #infect of two sims
      let infect_val = this.simulations[this.simulationId].simulationData.statsInfo[0].value
      let infect_val_custom = this.customSimulation.simulationData.statsInfo[0].value
      // get #recovered of two sims
      let rec_val = this.simulations[this.simulationId].simulationData.statsInfo[1].value
      let rec_val_custom = this.customSimulation.simulationData.statsInfo[1].value
      // refrain the length of line charts.
      // if more than 20 timestamps are shown in the chart, shift it to avoid overflow problem
      if (this.infect_line_series[0].data.length >= 20) {
        this.infect_line_series[0].data.shift()
        this.infect_line_series[1].data.shift()
        this.recovered_line_series[0].data.shift()
        this.recovered_line_series[1].data.shift()
      }
      // append new numbers at the end of the curve
      this.infect_line_series[0].data.push([timestamp, infect_val])
      this.infect_line_series[1].data.push([timestamp, infect_val_custom])
      this.recovered_line_series[0].data.push([timestamp, rec_val])
      this.recovered_line_series[1].data.push([timestamp, rec_val_custom])
    }
  }
}
</script>

