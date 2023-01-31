<template>
  <div class="sim_param_padding">

    <b-card-group deck>

      <b-card
          border-variant="primary"
          header="Simulation Parameters:"
          header-bg-variant="primary"
          header-text-variant="white"
          align="center">

        <b-card-text v-b-tooltip.hover :title=modeMessage>Mode: {{ this.simulation.mode }} <template v-if="useComparison"> | <p> {{ this.comparisonSim.mode }} </p> </template></b-card-text>

        <b-card-text v-b-tooltip.hover :title=datasetMessage>Dataset: {{ this.simulation.dataset }} <template v-if="useComparison"> | {{ this.comparisonSim.dataset }} </template></b-card-text>

        <b-card-text v-b-tooltip.hover :title=seedNodeMessage>Seed Node: {{this.simulation.seedNode}} <template v-if="useComparison"> | {{ this.comparisonSim.seedNode }} </template></b-card-text>

        <b-card-text v-b-tooltip.hover :title=blockProbabilityMessage> Block Probability:  {{ getValue(this.simulation.blockProb, 100) }} <template v-if="useComparison"> | {{ getValue(this.comparisonSim.blockProb, 100) }} </template> </b-card-text>

        <b-card-text v-b-tooltip.hover :title=recoveryRateMessage>Recovery Rate: {{ getValue(this.simulation.recoveryRate, 100) }} <template v-if="useComparison"> | {{ getValue(this.comparisonSim.recoveryRate, 100) }} </template></b-card-text>

        <b-card-text v-b-tooltip.hover :title=infectRateMessage>Infect Rate: {{ getValue(this.simulation.infectRate, 100) }} <template v-if="useComparison"> | {{ getValue(this.comparisonSim.infectRate, 100) }} </template></b-card-text>

      </b-card>
    </b-card-group>
  </div>
</template>

<script>

export default {
  // Take as prop a simulation object that's directly linked to the state of the web-application.
  // This means that when the parameters are changed in the simulation params, the parameters
  // are also changed is the application state
  props: {
    simulation: Object,
    comparisonSim: Object,
    useComparison: Boolean
  },
  methods: {
    getValue(value, multiplier) {
      return value / multiplier
    }
  },
  data() {
    return {
      // When user hover the mouse over the text on parameter panel, these instruction will appear
      datasetMessage: "Choose from 6 different datasets of real world temporal physical contact networks",
      modeMessage: "Choose from 13 different mitigation strategies",
      seedNodeMessage: "Choose the 'patient zero', the first one in the temporal network being infected",
      blockProbabilityMessage: "Choose the probability a link between two individuals are blocked",
      infectRateMessage: "Choose the probability an individual get infected when contact with a patient",
      recoveryRateMessage: "Choose the probability an infected individual recover in the next time stamp"
    }
  }
}
</script>
