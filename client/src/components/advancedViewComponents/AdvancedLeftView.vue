<template>
  <div class="advanced_left_view">
    <SimulationParams class="" :simulation="simulation" :use-comparison="useComparison" :comparison-sim="comparisonSim"/>
    <AdvancedViewButtons :use-comparison="useComparison" class="" :simulation="simulation"
                         :comparison-sim="comparisonSim"></AdvancedViewButtons>

    <div class="left_view_padding">
      <b-form-input class="left_view_padding b-table-stacked-md" id="range-2"
                    v-model="simSpeed" type="range" :min="min" :max="max"
                    step="1"></b-form-input>
      <div class="mt-2">Simulation Speed Interval: {{ simulation.simulationData.visualisationSpeed }} ms</div>
    </div>

  </div>
</template>


<script>
import AdvancedViewButtons from "@/components/visualisationComponents/AdvancedViewButtons";
import SimulationParams from "@/components/visualisationComponents/SimulationParams";

export default {
  props: {
    simulation: Object,
    comparisonSim: Object,
    useComparison: Boolean
  },
  components: {SimulationParams, AdvancedViewButtons},
  data() {
    return {
      simSpeed: 500,
      // simulation speed interval (for user to choose, shows how fast the network involves)
      min: 150,
      max: 2500
    }
  },
  watch: {
    simSpeed: function (val) {
      // update the simulation speed in all components
      if (this.useComparison)
        this.simulation.simulationData.visualisationSpeed = this.comparisonSim.simulationData.visualisationSpeed = val
      else
        this.simulation.simulationData.visualisationSpeed = val
    }
  }

}
</script>
