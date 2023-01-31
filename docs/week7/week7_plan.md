# Week plan 7

## Last week
* Implement a network visualization feature that a random seed node will be selected at the beginning of the network evolvement and show how it affects the whole network along the timeline.
* Read data result calculated by simulation running on the server.
* Implement Redis cache so that users are able to see the result of simulation without too much delay. 


## This week
* Again, discuss with the client and try to make CI work. If the client cannot provide any useful help, we can discard requirements regarding the CI.
* Write JavaScript & Python tests on client side.
* Make Next/Previous button working with the data read from the server.
* Make users able to select a certain timestamp and see the network at that timestamp by reading the simulation data from server.
*  Allow the user to compare multiple instances of the same simulation aka Seed Nodes
  The user will have available the following structures:
- [x] All features below are finished
    - [x] Dropdown Menu that allows choosing the visualisation for each seed node (#57)
    - [x] Simulation Stats that auto-render when the seed node is changing (#59)
    - [x] The main page will have the option to see this simulation but without advanced stats (#60)
    - [x] Change the Backend to deliver data about the children (#61)
* Store Simulation data into the state class
  The following sub-features will be implemented in order to achieve the parent issue (current one):
- [x] All features below are finished
    - [x] Store the data in a persistent way (the data won't be deleted when the view changes) (#62)
    - [x] Link the parameters of the simulation request to the APIs (#63)
    - [x] Use the stored data in all the available views which use the Visualisation Component. (#64)


## Improvements
* We made more commits & merge requests by splitting tasks into atomic units.

## Problems Encountered
* Workloads among all team members are still not balanced. 
