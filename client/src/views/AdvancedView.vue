<template>
  <div class="advanced-view">
    <NavigationBar/>
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-2">
          <StatsBar :statsInfo="this.simulations[simulationId].simulationData.statsInfo"
          />
        </div>
        <div class="col-md-10">
          <div class="container-fluid">
            <div class="row">
              <div class="col-md-10">
                <SimulationVisualisation :simulation="this.simulations[simulationId]"
                                         :useReady="false"
                                         ref="simulationVisualisation"/>
              </div>
              <div class="col-md-2">
                <AdvancedLeftView :use-comparison="false" :simulation="this.simulations[simulationId]"/>
              </div>
            </div>
            <div class="row">

              <SimulationNavigationButtons :simulation="this.simulations[simulationId]" @start-sim="startSim"
                                           @stop-sim="stopSim"
                                           @reset-sim="resetSim"
              ></SimulationNavigationButtons>
            </div>
          </div>

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
  name: 'AdvancedView',
  components: {
    AdvancedLeftView, NavigationBar, SimulationVisualisation, SimulationNavigationButtons, StatsBar
  },
  data() {
    return {
      simulationId: this.$route.params.id
    }
  },
  mounted() {
  },
  computed: {
    ...mapState(['simulations'])
  },
  methods: {
    // link the buttons with their implementation in the child (SimulationVisualisation)
    // the execution tree looks like this:
    // SimulationNavigationButtons - emits start event
    // Parent (this view) catches the event
    // Parent sends the event to the SimulationVisualisation component
    startSim() {
      this.$refs.simulationVisualisation.start()
    },
    stopSim() {
      this.$refs.simulationVisualisation.stop()
    },
    resetSim() {
      this.$refs.simulationVisualisation.reset()
    }
  }
}
</script>

