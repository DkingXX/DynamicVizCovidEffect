<template>
  <div>
    <button class='draw' @click="checkSim"> Click for sim</button>
  </div>

</template>


<script>
//import D3Network from "vue-d3-network";
import * as req from '../../helpers/request'

export default {
  name: "SimulationVisualizationSeeds",
  props: {simulation: Object},
  components: {
    //D3Network,
  },
  methods: {
    checkSim() {
      let current = this
      console.log('clicked checksim')
      console.log(this.simulation.simulationData.data)
      if (!this.simulation.simulationData.data.populated) {
        console.log('if statement')
        // get simulation parameters from ParamChooser and send to api
        req.run_sim(this.simulation.dataset, this.simulation.block_prob, this.simulation.recoveryRate, this.simulation.start_node, this.simulation.infect_rate, this.simulation.mode,
            function (err, body) {
              if (err) {
                console.log(err)
              } else {
                console.log('Simulation Data Received')
                current.storeBody(body)
              }
            })
      }

    },
    storeBody(body) {
      this.simulation.simulationData.data.contents = body;
      alert('body received and stored')
    }
  }
  ,
  mounted() {
  }
}
</script>
