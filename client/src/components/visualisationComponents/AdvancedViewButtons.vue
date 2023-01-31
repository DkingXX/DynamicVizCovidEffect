<template>
  <div class="advanced-view-buttons">
    <button v-b-modal.modalChooser class="classic-button draw meet">Change Parameters</button>

    <b-modal id="modalChooser" @ok="handleOKParam" @cancel="handleCancelParam"
             title="Modify the simulation parameters">

      <div class="container-fluid">
        <div class="row">
          <ParamChooser :class="getClass()" :show-buttons="false" :simulation="simulation"
                        :component-title="getTitle(0)"/>
          <ParamChooser :class="getClass()" v-if="useComparison" :show-buttons="false" :simulation="comparisonSim"
                        :component-title="getTitle(1)"/>
        </div>
      </div>
    </b-modal>
  </div>
</template>


<script>
import ParamChooser from "@/components/generalUseComponents/ParamChooser";

export default {
  name: 'AdvancedView',
  // take the simulation as a prop. The sim. is directly linked to the state
  // this means that when you change the simulation the state also changes
  // for all the web-application and subcomponents
  props: {
    simulation: Object,
    comparisonSim: Object,
    useComparison: Boolean
  },
  components: {ParamChooser},
  data() {
    return {}
  },
  methods: {
    // handle the ok button in the popup window present in this component (modalChooser)
    // nothing should happen here at the moment
    handleOKParam() {
      console.log("modal ok was pressed in param chooser advanced view");
    },
    // handle the cancel button in the popup window present in this component (modalChooser)
    handleCancelParam() {
      console.log("modal cancel was pressed in param chooser advanced view");
    },
    getClass() {
      // divide the grid into two if we are in the comparison mode
      // if not take all the space available
      if (this.useComparison)
        return 'col-md-6 center_left_view param-border'
      else
        return 'col-md-12 center_left_view'
    },
    getTitle(simNr) {
      // get title when it is in the comparison mode
      if (!this.useComparison)
        return ''
      else if (simNr === 1)
        return 'Right Simulation:'
      else
        return 'Left Simulation:'
    }

  }
}
</script>
