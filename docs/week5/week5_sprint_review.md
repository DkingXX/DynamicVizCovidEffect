# Sprint review 5

| User Story | Task     | Assigned to | Expected duration (hours) | Actual duration (hours) | Done  | Notes |
| :--------- | :------- | :---------- | :------------------------ | :---------------------- | :---- | :---- |
|Users must be able to access an advanced view of the simulation.|The user is able to see statistics about the spreading and a live simulation, based on the contact network (parameters).|Andrei & Ina|12|13|Yes|The time is for each individual (person).|
|Make the advanced view simulation modal.|The advanced view can be used in every component of the website.|Andrei & Ina|3|3|Yes|N/A|
|Separate all the advanced view component.|Develop the elements in a way so the code can be reused.|Andrei & Ina|4|4|Yes|The components can be used independently.|
|Users must be able to see the network in both classic view & advanced view.|Merge the demo of the network to the GUI.|Xiangyu & Zenan|4|6|Yes|N/A
|Users should be able to view the network at a specific timestamp.|Make a timeline that can be scrolled & make the timestamp that can be selected.|Xiangyu & Zenan|6|8|No|We made design choices on how to visualize this due to large amount of timestamp. We finally determined to divide the timeline into a lot of small sections, each contains a certain amount of timestamps so that the timeline will not leak the screen.|
|Users must be able to see a clean, simple network.|Simplify the network by removing the connection(s) set up during the last timestamp.|Xiangyu & Zenan|6|8|No|We have to take 'Next' & 'Previous' button into consideration so it is not that easy to do. It will be solved during the beginning of the next sprint.|
|Users must be able to start/stop/go to the network in next/previous timestamp/reset the network in advanced view.|Merge the function of each button to corresponding button in advanced view.|Xiangyu & Zenan|2|4|Yes|N/A
|With some request the server won't work|Fix the bugs on the server|Ziang|2|6|Yes|The bugs has been resolved|
|Front end need to request info from backend|create request with gzip decompression|Ziang|5|30|Yes|Due to knowledge limited and bug in some packages that task has significant delay|
|Fix CI pipeline|CI task with pipeline|Ziang|10|10+|No|CI still not working, tried to use gcp k8s however tudelft does not allow to link our own k8s, have to create a docker image with my own command that I don't know how to do that.|


## Improvements from last sprint

* We made a sprint review this time to reformat retrospective.
* We distributed our tasks in a more balanced way regarding the workload. 
* We communicate more within the team, with more meetings.


## Improvements from last sprint

* We distributed our tasks in a more balanced way regarding the workload.
* We asked for more help from other team members when encountering problems that cannot be solved by selves. 
* We made more commits & merge requests by splitting tasks into atomic units.
* We made improvements on using the issue board.
