# Week plan 8

## Last week
* Improve the GUI on making a timeline that contains a point for users to scroll to certain timestamp and view the network at that specific timestamp. Also simplify the network by removing/adding connection(s) from previous/next timestamp.
* Implement a network visualization feature that a random seed node will be selected at the beginning of the network evolvement and show how it affects the whole network along the timeline.
* Again, discuss with the client and try to make CI work. If the client cannot provide any useful help, we can discard requirements regarding the CI.
* Write JavaScript & Python tests on client side.
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


## This week
* Fix Parameter Requests (BUG)
* Fix and Improve the Navigation Buttons and Timeline #50
* Fix State Data share between simulations (BUG) #72
* Adjust the CI
* Backend Tests (sim request tests)
* Simulation Speed Adjustments #36
* New Requirement (this week + next week)
* Loading Screen that allows the user to see that the client waits for data from the backend #68
* Improve the backend speed #73
* Include the time spent for each issue on GitLab.

## Improvements
* Estimated time spent for each issue included on GitLab.
* The improvements and issues can be seen in the sprint review associated with this week 8 plan.
