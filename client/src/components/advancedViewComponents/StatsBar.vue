<template>
  <div class="stats_bar">

    <div class="row" v-for="(stats,index) in this.statsInfo" :key="index">

      <StatsCard>

        <div class="icon-big text-center" :class="`icon-${stats.type}`" slot="header">

          <img class='icon-big' :src="stats.icon">
        </div>

        <div class="numbers" slot="content">
          <p>{{ stats.name }}</p>
          {{ getConcatValue(index) }}
        </div>

        <div class="stats" slot="footer">
          <i :class="stats.icon"></i> {{ stats.moreInfo }}
        </div>

      </StatsCard>
    </div>
  </div>
</template>

<script>

import StatsCard from "@/components/stats/StatsCard";

export default {
  methods:{
    getConcatValue(index){
      if (this.isReset === true) return '0 | 0'
      // check if user is currently in advanced view or in comparison view,
      // if in advanced view, simply return sim 1 stats
      if (this.customStatusInfo === undefined || this.customStatusInfo === null ||
          this.customStatusInfo.length === 0)
        return this.statsInfo[index].value
      // concat stats info for two compared simulations
      return this.statsInfo[index].value + ' | ' + this.customStatusInfo[index].value
    }
  },
  props: {
    statsInfo: Array,
    customStatusInfo: Array,
    isReset: Boolean
  },
  components: {StatsCard},
  data() {
    return {}
  }
}
</script>
