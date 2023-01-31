<template>
  <div class="home-view-container">
    <button class="classic-button draw meet" @click="handleAddSimulation">Add new simulation</button>

    <SimulationPanel v-for="(sim,index) in simulations"
                     :key="index" :id="index" :simulation="sim"
                     :simId="index" @delete-event="handleDelete"/>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import SimulationPanel from "@/components/visualisationComponents/SimulationPanel";

export default {
  name: 'home',
  components: {SimulationPanel},
  data() {
    return {}
  },
  computed: {
    ...mapGetters([]),
    ...mapState(['simulations', 'modes', 'datasets','datasetsMetadata'])
  },
  methods: {
    ...mapActions(['addSimulation', 'deleteSimulation']),
    // action to add new sim
    handleAddSimulation() {
      this.addSimulation()
    },
    // action to delete a sim
    handleDelete(event, value) {
      this.deleteSimulation(value)
    }
  }
}
</script>
