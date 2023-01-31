export default {
    // commits that perform the actions in the mutations.js file
    addSimulation: ({commit}) => {
        commit('appendSimulation')
    },
    deleteSimulation: ({commit}, id) => {
        commit('removeSimulation', id)
    },
    resetSimulation: ({commit}, simulation) => {
        commit('resetSimulation', simulation)
    },
    storeDatasets: ({commit}, datasets) => {
        commit('setDatasets', datasets)
    },
    storeModes: ({commit}, modes) => {
        commit('setModes', modes)
    },
    storeDatasetsMetadata: ({commit}, metadata) => {
        commit('setDatasetMetadata', metadata)
    }

}
