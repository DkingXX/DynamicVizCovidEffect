<template>
  <div class="param-chooser-container">

      <h5 class="justify-content-center">{{ componentTitle }}</h5>

    <b-form-group id="input-group-1" label="Mode:" v-b-tooltip.hover :title=modeMessage>
      <b-form-select v-model="simulation.mode" :options=capitalize></b-form-select>
    </b-form-group>

    <b-form-group id="input-group-2" label="Datasets:" v-b-tooltip.hover :title=datasetMessage>
      <b-form-select
          id="input-datasets"
          v-model="simulation.dataset"
          :options="this.datasets"
          required
      ></b-form-select>
    </b-form-group>

    <b-form-group id="input-group-3" label="Seed node:" v-b-tooltip.hover :title=seedNodeMessage>
      <b-form-select
          id="input-seedNode"
          v-model="simulation.seedNode"
          :options=chooseSeedNode
          required
      ></b-form-select>
    </b-form-group>

    <b-form-group id="input-group-4" label="Block Probability:" v-b-tooltip.hover :title=blockProbabilityMessage>
      {{ getValue(this.simulation.blockProb) }}
      <b-form-input id="input-block-probability" class="formControlRange" v-model="simulation.blockProb" type="range"
                    min="0" max="1, step='0.01"></b-form-input>

    </b-form-group>

    <b-form-group id="input-group-5" label="Recovery rate:" v-b-tooltip.hover :title=recoveryRateMessage>
      {{ getValue(this.simulation.recoveryRate) }}
      <b-form-input id="input-block-probability" class="formControlRange" v-model="simulation.recoveryRate" type="range"
                    min="0" max="1, step='0.01"></b-form-input>

    </b-form-group>

    <b-form-group id="input-group-6" label="Infect Rate:" v-b-tooltip.hover :title=infectRateMessage>
      {{ getValue(this.simulation.infectRate) }}
      <b-form-input id="input-block-probability" class="formControlRange" v-model="simulation.infectRate" type="range"
                    min="0" max="1, step='0.01"></b-form-input>
    </b-form-group>

    <div v-if='showButtons' class="buttons">
      <button v-b-tooltip.hover :title=startSimulationMessage
              class="buttons-dist draw meet" @click="start">Start Simulation
      </button>
      <button v-b-tooltip.hover :title=resetSimulationMessage
              class="buttons-dist spin thick" @click="reset">Reset
      </button>
    </div>

  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'

export default {
  data() {
    return {
      // the messages that are displayed when the user hovers the start simulation and reset simulation
      startSimulationMessage: "Press here to start the simulation",
      resetSimulationMessage: "Press here to reset a simulation and its parameters",

      // the messages will be displayed when user move the mouse over the dropdown menu or parameter axes in parameter chooser
      modeMessage: "Choose from 13 different mitigation strategies",
      datasetMessage: "Choose from 6 different datasets of real world temporal contact networks",
      seedNodeMessage: "Choose the 'patient zero', the first one in the temporal network being infected",
      blockProbabilityMessage: "Choose the probability that two individuals no longer meet (based on the mitigation strategy chosen above)",
      recoveryRateMessage: "Choose the probability an infected individual recovers from the disease",
      infectRateMessage: "Choose the probability that a covid infected person can spread the virus to another",
    }
  },
  props: {
    simulation: Object,
    showButtons: Boolean,
    componentTitle: String
  },
  methods: {
    // when the user resets the simulation, the parameters and simulation data are set to null/0
    ...mapActions(['resetSimulation']),
    start() {
      console.log('event sent from param chooser')
      this.$emit('start-sim')
    },
    reset() {
      this.resetSimulation(this.simulation)
    },
    // getValue displays a value in percentage based on the sliding bars present in this component
    getValue(currentValue) {
      return currentValue / (100)
    }
  },
  computed: {
    // The modes in which the simulation can run.
    // aka. mitigation strategies
    ...mapState(['simulationStructure', 'datasets', 'modes', 'datasetsMetadata']),
    capitalize() {
      let result = []
      // take each word and capitalize it
      this.modes.forEach((i) => {
        let str = ""
        i.split(" ").forEach((j) => {
          str += j.charAt(0).toUpperCase() + j.slice(1) + " ";
        })
        // remove the extra-space at the end
        str = str.substr(0, str.length - 1)
        result.push(str)
      })
      // return the capitalize result
      return result
    },
    // method to only allow user to choose seed node after selecting the dataset
    chooseSeedNode() {
      let result = []
      if (this.simulation.dataset === '') {
        return ['Please select a dataset before choosing seed node']
      } else { // add seed node of a specific dataset in format of numbers to drop down menu
        for (let i = 0; i < this.datasetsMetadata['sizes'][this.simulation.dataset]; i++) {
          result.push(i)
        }
      }

      return result
    }
  }
}
</script>
