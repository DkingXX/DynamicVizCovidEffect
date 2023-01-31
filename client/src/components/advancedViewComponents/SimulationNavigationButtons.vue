<template>
  <div class="simulation_navigation_buttons">

    <div class="container-fluid">
      <div class="row">
<!--        <b-progress v-b-tooltip.hover :title=progressBarText class="w-50"-->
<!--                    :value="simulation.simulationData.simulationProgress"-->
<!--                    :max="simulation.simulationData.maxProgress" :striped="this.stripped" :variant="this.variant"-->
<!--                    show-progress animated></b-progress>-->
        <b-progress v-b-tooltip.hover
                    style="width:100%"
                    :title=progressBarText
                    :value="simulation.simulationData.simulationProgress"
                    :max="simulation.simulationData.maxProgress"
                    :striped="this.stripped"
                    :variant="this.variant"
                    show-progress animated>
        </b-progress>
      </div>

      <div class="row simulation_navigation_buttons_align">

        <button :disabled="simulation.simulationData.isRunning" class="classic-button draw meet" @click="startSim">
          Start
        </button>

        <button :disabled="!simulation.simulationData.isRunning" class="stop-reset-button draw meet" @click="stopSim">
          Stop
        </button>

        <button class="stop-reset-button draw meet" @click="resetSim">
          Reset
        </button>

      </div>

    </div>
  </div>
</template>

<script>
export default {
  props: {
    simulation: Object
  },
  methods: {
    startSim() {
      this.$emit('start-sim')
    },
    stopSim() {
      this.$emit('stop-sim')
    },
    resetSim() {
      this.$emit('reset-sim')
    }
  },
  data() {
    return {
      // variable that stores the timestamp progress
      // this variable will move in the state when it is ported to the server
      // implementation
      stripped: true,
      variant: 'info',
      progressBarText: "The simulation progress over time \n based on how people meet in the real world"
    }
  }
}
</script>
