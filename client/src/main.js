import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import {Plugin} from 'vue-responsive-video-background-player'

import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import './assets/sass/index.sass'

// make use of the state at initialization
import {mapActions, mapState} from 'vuex'
//make use of the request to get data at initialization
import * as req from "./helpers/request";

// register eCharts components globally
// import c from './helpers/echarts_core';
// eslint-disable-next-line
const c = require('./helpers/echarts_core');

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
Vue.use(Plugin);

Vue.config.productionTip = false

new Vue({
    router,
    store,
    render: h => h(App),
    computed: {
        ...mapState(['simulations', 'datasets', 'modes', 'simulationStructure'])
    },
    mounted() {
        // when the Application starts, create a new simulation with empty parameters
        let firstSim = Object.assign({}, this.simulationStructure)
        this.simulations.push(firstSim)

        // WITH THE FOLLOWING GET METHODS THE BACKEND CAN ADJUST THE SIMULATION STRATEGIES AND DATASETS
        // WITHOUT MODIFYING ANYTHING ON THE CLIENT SIDE

        // when the Application starts, get the datasets from the server in order to be displayed and used in the components
        const current = this;
        req.general_request('GET', 'datasets', null, function (err, body) {
            if (err) {
                console.log(err)
            } else {
                console.log('Dataset Data Received')
                // when the callback finishes, store the datasets
                current.storeDatasets(body)
            }
        });

        // when the Application starts, get the available strategies from the server in order to be displayed and used in the components
        req.general_request('GET', 'strategies', null, function (err, body) {
            if (err) {
                console.log(err)
            } else {
                console.log('Dataset Strategies Received')
                // when the callback finishes, store the strategies
                current.storeModes(body)
            }
        });

        // when the Application starts, get the number of possible seed nodes
        req.general_request('GET', 'datasetMetadata', null, function (err, body) {
            if (err) {
                console.log(err)
            } else {
                console.log('Datasets Metadata Received')
                // when the callback finishes store the nodeCount
                current.storeDatasetsMetadata(body)
                console.log(body)
            }
        });

    },
    methods: {
        // map the actions that store the items retrieved from the backend
        ...mapActions(['storeDatasets', 'storeModes', 'storeDatasetsMetadata'])
    }
}).$mount('#app')
