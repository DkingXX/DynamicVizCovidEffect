import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import AdvancedView from '../views/AdvancedView'
import ComparisonView from "../views/ComparisonView";


Vue.use(VueRouter)
// define paths for all views
const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: About
    },
    {
        path: '/advanced/:id',
        name: 'Advanced',
        component: AdvancedView
    },
    {
        path: '/comparison/:id',
        name: 'Comparison',
        component: ComparisonView
    }
]

const router = new VueRouter({
    routes
})

export default router
