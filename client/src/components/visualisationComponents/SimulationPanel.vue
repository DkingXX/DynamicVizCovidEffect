<template>

  <div class="simulation-panel-container">
    <div class="container-fluid">

      <div class="row">

        <div class="col-md-2">
          <ParamChooser @start-sim='startSimulation' :showButtons='true' :simulation="simulation"/>
        </div>
        <div class="col-md-10">

          <div id="SimulationNodes">
            <SimulationVisualisation :simulation="this.simulation"
                                     :useReady="false"
                                     ref="simulationVisualisation">
            </SimulationVisualisation>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-md-4">
          <button v-b-tooltip.hover :title=deleteSimulationMessage class="buttons-dist circle spin thick"
                  @click="deleteCurrentSimulation">Delete
          </button>
        </div>

        <div class="col-md-4">
          <button v-b-tooltip.hover :title=advancedViewButtonMessage class="buttons-dist draw" @click="routeToAdvanced">
            Advanced View
          </button>
        </div>

        <div class="col-md-4">
          <button v-b-tooltip.hover :title=comparisonViewButtonMessage class="buttons-dist draw" @click="routeToComparison">
            Comparison View
          </button>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
import ParamChooser from "@/components/generalUseComponents/ParamChooser";
import SimulationVisualisation from "./SimulationVisualisation";

export default {
  name: 'SimulationNodes',
  components: {
    ParamChooser, SimulationVisualisation
  },
  props: {
    simulation: Object,
    simId: Number
  }
  ,
  methods: {
    deleteCurrentSimulation() {
      // when the user presses the delete button, an event is emitted and the parents are expected
      // to catch it and delete the simulation accordingly to the simulation id
      this.$emit('delete-event', this.id)
    },
    startSimulation() {
      console.log("start sim start")
      this.$refs.simulationVisualisation.start()
    },
    fullScreen() {
      // this function should be called when the user wants to go fullscreen
      //TODO: implement the fullScreen functionality
      alert('THIS SHOULD OPEN A FULL SCREEN PANEL WITH THE VISUALISATION')
    },
    routeToAdvanced() {
      // route the current simulation into the advanced panel accordingly with the data present in the
      // state class
      this.$refs.simulationVisualisation.reset()
      this.$router.push('advanced/' + this.simId)
    },
    routeToComparison() {
      // route the current simulation into the advanced panel accordingly with the data present in the state class
      this.$refs.simulationVisualisation.reset()
      this.$router.push('comparison/' + this.simId)
    },

  },
  data() {
    return {
      // messages that are displayed when user hover the buttons
      advancedViewButtonMessage: "Press here to see this simulation in the advanced mode",
      deleteSimulationMessage: "Press here to delete the current simulation",
      comparisonViewButtonMessage: "Press here to compare different simulation"
    }
  }
}
</script>
