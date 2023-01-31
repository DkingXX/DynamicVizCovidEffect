//declearation of danfojs and numjs
const dfd = require("danfojs-node")
const nj = require('numjs');

let mit1 = dfd.read_csv("/public/data/mit1.csv");
let mit2 = dfd.read_csv("/public/data/mit2.csv");
let hs11 = dfd.read_csv("/public/data/hs11.csv");
let hs12 = dfd.read_csv("/public/data/hs12.csv");
let work1 = dfd.read_csv("/public/data/work1.csv");
let work2 = dfd.read_csv("/public/data/work2.csv");

let dataset = { 'hs11': hs11, 'hs12': hs12, 'work1': work1, 'work2': work2, 'mit1': mit1, 'mit2': mit2 };

function makeArr(startValue, stopValue, cardinality) {
    var arr = [];
    var step = (stopValue - startValue) / (cardinality - 1);
    for (var i = 0; i < cardinality; i++) {
        arr.push(startValue + (step * i));
    }
    return arr;
}

function min_arg(a) {
    return a.indexOf(Math.min.apply(Math, a));
}

function infect_time(infect, dataset) {
    var interval = makeArr(Math.min(dataset["time"]), Math.max(dataset["time"]), 10000);
    var infect_frac = Array.fill.call({ length: 10000 }, 0);
    for (var i = 0; i < 10000; i++) {
        var timeList = nj.array(dataset["time"]) < interval[i];
        var index = min_arg(timeList);
        infect_frac[i] = nj.mean(infect[index]);
    }
    return infect_frac;
}

function iterate(dataset, i) {
    dataset['time'] -= Math.min(dataset['time']);
    var dataset_ = dataset.copy();
    var T = Math.max(dataset["time"]);
    for (var x = 0; x < i; x++) {
        dataset_["time"] = dataset_["time"] + T;
        dataset = dfd.concat([dataset,dataset_]);
    }
    return dataset;
}

class Model {
    constructor(contacts,nodes,block_prob=0.1,rec=0.1,time_w=null) {
        this.contacts = contacts
        this.nodes = nodes
        this.block_prob = block_prob
        this.people = dfd.unique(this.contacts[["p1","p2"]])
        this.n = this.people.size
        this.cure = rec/(3600*24)
        this.start_t = Math.min(this.contacts['time'])
        this.end_t = Math.max(this.contacts['time'])
        this.T5 = this.start_t + 0.5*(this.end_t-this.start_t)
        this.block_prob = {}
        let p2id = {}
        
        
    }
}
