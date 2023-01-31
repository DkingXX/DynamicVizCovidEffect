const request = require('request');

export function run_sim(dataset = "hs11", block_prob = 0.3, recovery = 0.1,
                        start_node = 0, infect_rate = 0.01, mode = "degree product",
                        callback) { // default parameters if no has been chosen
    console.log('runsim Running')
    const options = {
        'method': 'POST',
        'uri': 'http://localhost:8000/sim',
        encoding: null,
        gzip: true,
        body: JSON.stringify({
            "dataset": dataset,
            "block_prob": block_prob,
            "recovery": recovery,
            "start_node": start_node,
            "infect_rate": infect_rate,
            "mode": mode
        })

    };

    request(options
        , function (error, response, body) {
            console.log('request init')
            if (error || response.statusCode !== 200) {
                console.log('error request')
                return callback(error || {statusCode: response.statusCode});
            }
            callback(null, JSON.parse(body))
        });
}


export function general_request(method, endpoint, body, callback) {
    console.log('general Request')
    // take general options passed in the method
    const options = {
        'method': method,
        'uri': 'http://localhost:8000/' + endpoint,
        encoding: null,
        gzip: true,
        body: body
    };

    // request the data and pass it in the callback function
    request(options
        , function (error, response, body) {
            console.log('request init')
            if (error || response.statusCode !== 200) {
                console.log('error request')
                // if it gets any error/status code, return it to the client side
                return callback(error || {statusCode: response.statusCode});
            }
            callback(null, JSON.parse(body))
        });
}
