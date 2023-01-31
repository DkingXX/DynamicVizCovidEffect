<template>
  <div class="stats_bar">

    <div class="row" v-for="(stats,index) in this.statsInfo" :key="index">

      <StatsCard>

        <div class="icon-big text-center" :class="`icon-${stats.type}`" slot="header">

          <img class='icon-big' :src="stats.icon">
        </div>

        <div class="numbers" slot="content">
          <p class="text-wrapping">{{ stats.name }}
          </p>
          {{ stats.value }}
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
  props: {
    statsInfo: Array
  },
  components: {StatsCard},
  data() {
    return {}
  }
}
</script>
