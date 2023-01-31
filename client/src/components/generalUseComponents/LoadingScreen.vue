<template>
  <div class="fit-parent">
    <h4> {{ loadingMessage }} </h4>
    <d3-network :class="getSimulationClass()" :net-nodes="nodes" :net-links="links" :options="options"/>
  </div>
</template>


<script>
import D3Network from "vue-d3-network"

export default {
  name: "LoadingScreen",
  components: {
    D3Network
  },
  data() {
    return {
      run: true,
      loadingMessage: 'Loading',
      snapshot: [],
      nodes: [],
      links: [],
      options: {
        nodeSize: 80,
        nodeLabels: true,
        linkWidth: 3,
        resizeListener: true,
        force: 7000,
        fontSize: 15,
        linkLabels: true,
        strLinks: true
      },
      timer_status: "stop",
    }
  },
  methods: {
    getSimulationClass() {
      // get the css class based on the route
      return this.$route.name !== 'Comparison' ? 'fit-parent-general-purpose' : 'fit-parent'
    },
    sleep(ms) {
      // wait a certain ms to complete another loading cycle
      return new Promise(resolve => setTimeout(resolve, ms));
    },
    resetLoadingAnimation() {
      this.links = []
      this.nodes[1]._color = "green"
    },
    initNodes() {
      // init the loading nodes
      this.nodes.push({id: 0, _color: "red", name: "Infected"})
      this.nodes.push({id: 1, _color: "green", name: "Non-Infected"})
      this.nodes.push({id: 2, _color: "purple", name: "Recovered"})

    }
  },
  async mounted() {
    this.initNodes()
    let counter = 0
    while (this.run) {
      // if (this.loadingMessage.length === 10)
      // create the loading message and build it
      if (this.loadingMessage === 'Loading...')
        this.loadingMessage = 'Loading'
      else
        this.loadingMessage += '.'

      // establish links in order to 'simulate' the loading
      if (counter === 1) {
        this.links.push({
          sid: this.nodes[0],
          tid: this.nodes[1],
          _color: "red",
        });
        // this.nodes[1]._color = 'red'
      }

      if (counter === 2) {
        this.links.push({
          sid: this.nodes[0],
          tid: this.nodes[2],
          _color: "purple",
        });
      }

      if (counter === 3)
        this.links.push({
          sid: this.nodes[2],
          tid: this.nodes[1],
          _color: "green",
        });

      // reset the links
      if (counter === 4) {
        counter = 0
        this.resetLoadingAnimation()
      }

      counter++
      await this.sleep(750);


    }
  }

}
</script>
