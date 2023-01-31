# Server Manual

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Redis Cache](#redis-cache)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- Covid-19 was found in Wuhan last year. It has caused a global pandemic for more than one year.
  Transmission of this virus occurred mostly in close contact with another person. Researchers from
  TU Delft developed a model that analyzes the spreading of Covid-19 with temporal networks.
  To help researchers and society better understand this model, we decided to visualize it.
  With the visualization of this model, we can help the society understand the importance of quarantine measures and contact mitigation strategies.
- This is backend for our Covid-19 Simulator.
- With this backend, you can input simulation parameter and get infect and recovery list.


## Technologies Used
- Numpy - 1.19.2
- Pandas - 1.1.3
- Networkx - 2.5
- tqdm - 4.50.2
- fastapi - 0.65.0
- pydantic - 1.8.1

## Features
- Pre-calculated data
- RestAPI
- Visualization the virus spreading process under simulation in temporal networks
- Overloading prevention
- Docker
- No database
- K8s supported
- Gzip on reducing network traffic
- Redis cache


## Usage

The first thing to do is to clone the repository:

```sh
$ git clone https://gitlab.ewi.tudelft.nl/cse2000-software-project/2020-2021-q4/cluster-13/migrate-epidemic-spreading.git
$ cd migrate-epidemic-spreading
$ cd server
```


Then install the dependencies:

```sh
$ pip install -r requirements.txt
```

If you have python2 package, please use:
```sh
$ pip3 install -r requirements.txt
``` 

Once `pip` has finished downloading the dependencies:
```sh
$ uvicorn main:app --reload
```
And navigate to `http://127.0.0.1:8000/`.
If you see `The simulator is working. Please visit /doc for swagger page.` Then the server is running.

(Please note that the first startup of the server may be a quite slow. It takes around 2-3 minutes until the server caches some necessary data)

## Redis Cache

Redis cache is implemented but purely optional.
To prevent computation of a simulation with the same parameters multiple times,
install and run a Redis server on port `6379` and our application will handle the requests for you.

You can choose the Redis version available in the repository, in the folder /redis, or
you can install one from the official Redis website. 

More info on how to install the Redis server on : `https://redis.io/download`


## Project Status

Project is: _finished_. 
Tests and cache have been added. The test coverage is 92%.

## API usage
Please navigate to `http://127.0.0.1:8000/doc` for API usage.

## Room for Improvement
Room for improvement:
- [x] Speed up simulation process.
- [x] Run simulation in comparison mode.
- [ ] Add simulation process to frontend.
- [ ] Prevent multiple requests at one time.

To be implemented:
- [x] Redis cache
- [x] Auto deploy CI/CD
- [x] Unit tests for coverage


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




