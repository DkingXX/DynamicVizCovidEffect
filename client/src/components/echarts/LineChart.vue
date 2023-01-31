  <template>
  <div>
    <v-chart :style="'height:' + this.height + 'px'" :option="c_option" />
  </div>
</template>

<script>
import { THEME_KEY } from "vue-echarts";
import 'echarts/theme/macarons'

export default {
  name: "Chart",
  props: {
    series: {
      type: Array,
      default: null,
    },
    title: {
      type: String,
      default: "Plot",
    },
    height: {
      type: Number,
      default: 400,
    },
  },
  provide: {
    [THEME_KEY]: 'macarons',
  },
  computed:{
    legendTitle(){ // legend title
      return this.series.map(o => o.name)
    }
  },
  data() {
    return {
      c_option: {
        xAxis: {
          type: "category",
          boundaryGap: false,
          minInterval: 250,
          showAllSymbol: true
        },
        yAxis: {
          type: "value",
          boundaryGap: [0, "20%"],
        },
        legend:{
          orient: 'vertical',
          left: 'left',
          data: this.legendTitle
        },
        title: {
          text: this.title,
          left: "center",
        },
        tooltip: {
          trigger: "axis",
          formatter: "{a} <br/>{b} : {c}",
        },
        series: this.series,
      },
    };
  },
};
</script>
