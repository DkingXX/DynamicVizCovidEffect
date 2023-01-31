# Client Manual

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Code Details](#code-details)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- Covid-19 was found in Wuhan last year. It has caused a global pandemic for more than one year.
  Transmission of this virus occurred mostly in close contact with another person. Researchers from
  TU Delft developed a model that analyzes the spreading of Covid-19 with temporal networks.
  To help researchers and society better understand this model, we decided to visualize it.
  With the visualization of this model, we can help the society understand the importance of quarantine measures and contact mitigation strategies.
- This is client for our Covid-19 Simulator.
- With this client you can run a simulations on the website.


## Technologies Used
- vue - 2.6.1
- bootstrap-vue - 2.21.2
- buffer - 6.0.3
- core-js - 3.6.5
- vue-d3-network - 0.1.28
- more details can be found in [package.json](./package.json)

## Features
- Visualization of the virus spreading process under simulation in temporal networks
- Customization on the simulation parameters
- Docker
- No database
- Comparison Views and statistics to depict different mitigation modes and strategies


## Usage

The first thing to do is to clone the repository:

```sh
$ git clone https://gitlab.ewi.tudelft.nl/cse2000-software-project/2020-2021-q4/cluster-13/migrate-epidemic-spreading.git
$ cd migrate-epidemic-spreading
$ cd server
```
This project requires Nodejs environment, if you don't have one, please go to [node.js](https://nodejs.org/en/) and follow [official install instruction](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

Then install the dependencies:

```sh
$ npm install
```

serve with hot reload at localhost:8080:
```sh
$ npm run dev
``` 

build for production with minification:
```sh
$ npm run build
```

build for production and view the bundle analyzer report:
```sh
$ npm run build --report
```

And navigate to `http://127.0.0.1:8080/`. for home page.

## Project Status

Project is: _Finished_ 

## Code Details
__Code Details__ can be found in [code source folder](./src/readme.md).

## Acknowledgements
- This project was inspired by TU Delft AI Lab.
- Appreciate for all the help Xunyi Zhao has given to us throughout the project.


## Contact
Created by:

[Andrei Ionescu](A.C.Ionescu-1@student.tudelft.nl)\
[Ina Lupu](G.A.Lupu@student.tudelft.nl)\
[Xiangyu Du](X.Du-1@student.tudelft.nl)\
[Zenan Guan](Z.Guan@student.tudelft.nl)\
[Ziang Qiu](z.qiu@student.tudelft.nl)


Feel free to contact us!




