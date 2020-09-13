# Chores Bot
This application collects a name and robot type from the types list in JSON file. For each, it should create a Robot of the type the user chooses, e.g. Larry, Bipedal. 

Given the list of tasks in Tasks.JSON, this application should then assign the Robot a set of five tasks, all of which complete after a duration that is in milliseconds. 


- Collects a name and robot type from user.
- Instantiate a Robot of the type provided by the user with the name provided by the user
  - for example: Bipedal, Larry
- Set up methods on Robot to complete tasks from the provided list

## Robot
Robot completes tasks depending on assignment.

## Tasks
Tasks have a description and an estimated time to complete.

## Types
```
{ 
  UNIPEDAL: 'Unipedal',
  BIPEDAL: 'Bipedal',
  QUADRUPEDAL: 'Quadrupedal',
  ARACHNID: 'Arachnid',
  RADIAL: 'Radial',
  AERONAUTICAL: 'Aeronautical'
}
```
## How to Run
python3 Robot.py

