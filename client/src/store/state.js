export default {
    // the datasets will be fetched from the server
    datasets: ['Fetching Data'],
    // the metadata will be fetched from the server
    datasetsMetadata: {'metadata': 'empty for now'},
    // the strategies will be fetched from the server
    modes: ['Fetching Data'],
    // the seedNodes will be fetched from the server
    seedNodes: ['Fetching Data'],
    // display at the beginning just one simulation
    simulations: [],
    /* the simulation structure that is used to store the data for every simulation in the application.
       every time a new simulation is created this structure will be the foundation for the implementation. */
    simulationStructure: {
        dataset: '',
        mode: '',
        seedNode: '',
        blockProb: 0,
        recoveryRate: 0,
        repeats: 0,
        iterations: 0,
        infectRate: 0,
        simulationData: { // simulation params in right panel of advanced view
            visualisationSpeed: 500,
            dataset: '',
            mode: '',
            seedNode: '',
            blockProb: 0,
            recoveryRate: 0,
            repeats: 0,
            iterations: 0,
            infectRate: 0,
            simulationProgress: 0,
            maxProgress: 0,
            isRunning: false,
            snapshotReady: false,
            data: {
                populated: false,
                started: false,
                contents: {}
            },
            statsInfo: [
                {
                name: 'Infected People:',
                value: '0',
                icon: require(`@/assets/images/Virus.png`),
                moreInfo: "The number of people infected (with red) since the simulation started "
                },
                {
                    name: 'Recovered People:',
                    value: '0',
                    icon: require(`@/assets/images/disinfectant.png`),
                    moreInfo: "The number of people recovered (with purple) since the simulation started"
                },
                {
                    name: 'Total number:',
                    value: '0',
                    icon: require(`@/assets/images/safety-suit.png`),
                    moreInfo: "The total number of persons that take place into the simulation"
                }
            ]
        }
    },

}
