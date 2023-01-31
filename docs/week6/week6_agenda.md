# Agenda

This is the agenda for 24th of May.

---

Date:           24/05/2021\
Main focus:     Discussing the current state\
Chair:          Zenan\
Note taker:     Xiangyu

Notes: N/A

# Opening
Present: Ina, Zenan, Andrei, Xiangyu, Ziang, Alves and Marco\
Absent: None

# Points of action

* Merge the visualization into the GUI (Done)
* Re-structure the project (Done)
* Compressing and de-compressing the simulation data (backend) (Done)
* Trying to make the CI working

# Action points for next week (Scrum board)
* Make the CI working
* Improve the GUI
* Improve the visualization
* Preparing for the midterm presentation (28/05/2021, 12:00 - 13:00)

# Questions for the TA
* How to make CI work: The CI is working during the midnight only
* Suggestions on what we have shown.
  + Sprint review.

# Question round
Are there any questions?

# Meeting Note
* Discussion on making CI work
  + The reason that CI doesn't work so far is that we are not able to upload docker image to TU Delft Gitlab. Our algorithm takes too much memory for Gitlab server to handle. 
  + Our solution is to run our own server and set up the environment there. 
  + The TA suggested either take standard linux image and install python on that, or discuss with the client, who should be able to provide the cluster for CI to be deployed.
  + Several clusters would be the optimal solution.
  
* Discussion on the GUI
  + We do not want to have several networks simultaneously in advanced view since running the simulation and showing the results takes too much memory. 
  
* Discussion on midterm presentation
  + Only TA, coach, and the client will be present during the presentation.
  + One of the course coordinators will join at the end of the presentation.
  
* Discussion on commit, merge request & the usage of Gitlab
  + It shows an improvement from last sprint.
  + We should try to spread the workload more equally for each day.
  + The 'open' list in issue board should contain all tasks listed in backlog of current sprint.
  + Add assignees to some issues that have already been closed. 
  + It is good to link issues with the user story, but they can be split into more atomic units.
  + We should add 'Must Have' list to the issue board.

# Questions and answers




