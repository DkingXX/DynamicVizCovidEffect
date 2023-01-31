export default {
    // CATCH the actions and perform mutations based on them:

    // append a new simulation based on the Simulation Structure
    appendSimulation: (state) => {
        console.log("mutations.js appendSimulation called ")
        // state['simulations'].push(Object.assign({}, state['simulationStructure']))
        state['simulations'].push(deepCopy(state['simulationStructure']))
    },
    // remove a simulation from the application
    // the id is sent by the actions
    removeSimulation: (state,
                       id) => {
        console.log("mutations.js removeSimulation called ")
        state['simulations'].splice(id, 1)
    },
    // just set the nodes in order to be used in props (v-bind auto update)
    setDatasets: (state, dataset) => {
        state['datasets'] = dataset
    },
    setModes: (state, modes) => {
        state['modes'] = modes
    },
    // eslint-disable-next-line no-unused-vars
    resetSimulation: (state, simulation) => {
        simulation = deepCopy(state['simulationStructure'])
        // simulation = Object.assign({}, state['simulationStructure'])
        // const mode = simulation.mode
        // simulation.mode = mode
    },
    setDatasetMetadata: (state, metaData) => {
        state['datasetsMetadata'] = metaData
    }
}

// note: replace Object.assign which is shallow copy to 'deepCopy'
function deepCopy(obj){
    let copyObj = Array.isArray(obj) ? [] : {}
    for(let key in obj) {
        copyObj[key] = typeof (obj[key]) === "object" ? deepCopy(obj[key]) : obj[key]
    }
    return copyObj
}