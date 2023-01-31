import ECharts from 'vue-echarts'
import { use } from 'echarts/core'

import Vue from 'vue'

// import echart modules
import {
    SVGRenderer,
    CanvasRenderer
} from 'echarts/renderers'
import {
    LineChart,
    BarChart,
    PieChart,
    ScatterChart,
    RadarChart,
    MapChart,
    TreeChart,
    TreemapChart,
    GraphChart,
    GaugeChart,
    FunnelChart,
    ParallelChart,
    SankeyChart,
    BoxplotChart,
    CandlestickChart,
    EffectScatterChart,
    LinesChart,
    HeatmapChart,
    PictorialBarChart,
    ThemeRiverChart,
    SunburstChart,
    CustomChart
} from 'echarts/charts'
import {
    GridComponent,
    PolarComponent,
    GeoComponent,
    SingleAxisComponent,
    ParallelComponent,
    CalendarComponent,
    GraphicComponent,
    ToolboxComponent,
    TooltipComponent,
    AxisPointerComponent,
    BrushComponent,
    TitleComponent,
    TimelineComponent,
    MarkPointComponent,
    MarkLineComponent,
    MarkAreaComponent,
    LegendComponent,
    DataZoomComponent,
    DataZoomInsideComponent,
    DataZoomSliderComponent,
    VisualMapComponent,
    VisualMapContinuousComponent,
    VisualMapPiecewiseComponent,
    AriaComponent,
    DatasetComponent,
    TransformComponent
} from 'echarts/components'

use([
    LineChart,
    BarChart,
    PieChart,
    ScatterChart,
    RadarChart,
    MapChart,
    TreeChart,
    TreemapChart,
    GraphChart,
    GaugeChart,
    FunnelChart,
    ParallelChart,
    SankeyChart,
    BoxplotChart,
    CandlestickChart,
    EffectScatterChart,
    LinesChart,
    HeatmapChart,
    PictorialBarChart,
    ThemeRiverChart,
    SunburstChart,
    CustomChart
]);

use([CanvasRenderer]);
use([SVGRenderer]);

use([
    GridComponent,
    PolarComponent,
    GeoComponent,
    SingleAxisComponent,
    ParallelComponent,
    CalendarComponent,
    GraphicComponent,
    ToolboxComponent,
    TooltipComponent,
    AxisPointerComponent,
    BrushComponent,
    TitleComponent,
    TimelineComponent,
    MarkPointComponent,
    MarkLineComponent,
    MarkAreaComponent,
    LegendComponent,
    DataZoomComponent,
    DataZoomInsideComponent,
    DataZoomSliderComponent,
    VisualMapComponent,
    VisualMapContinuousComponent,
    VisualMapPiecewiseComponent,
    AriaComponent,
    DatasetComponent,
    TransformComponent
]);


const chart = {
    proto : ECharts
}

// define properties on the prototype of vue
Vue.prototype.$chart = chart
// register echart component globally
Vue.component('v-chart', chart.proto)

import eLine from '../components/echarts/LineChart'

Vue.component('eLine', eLine)

export default chart
