import Vue from 'vue'
import Vuex from 'vuex'
// eslint-disable-next-line no-unused-vars
import state from './state'
// eslint-disable-next-line no-unused-vars
import mutations from './mutations'
// eslint-disable-next-line no-unused-vars
import actions from './actions.js'
// eslint-disable-next-line no-unused-vars
import getters from './getters'

Vue.use(Vuex)

export default new Vuex.Store({
  state,
  mutations,
  actions,
  getters
})
