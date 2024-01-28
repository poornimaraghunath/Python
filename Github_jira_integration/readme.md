# In this project will integrate Github with Jira which helps the developers to track the issues created in github.
   
      This project helps the developer to reduce the time spending on jira backlog creation because in this project when developer sees the issues created in github he can comment there only which can create jira backlog without logging into the jira.

#This feature will help when the QA team or any other team when working the github if they any find any bugs in the code they will create issue so developer once in a week or 2 days will login the github and check the issues . IIn that case of the issue is not valid they can close the issue there only  but if the issue is valid they need to work on it and track the time spent on it for that developer needs to spend time on creating jora backlog.

#For this developers has seeked the help from the devops team to automate this process 

#In this proccess github and jira are two resources need to interact  so for interaction will use python as bridge between them.

#In this if any comments /jira on the issue it will trigger the webhooks on github and provides the information about the issue to the python application deployed on Ec2.Github will provide the information in the form of json data to python application and then python application makes an api call to jira to cretae the backlog

#In this will learn how to create  jira backlog how to use jira apps and then how to write the python application using flask.
#Then will learn how to convert python application for flask and then how to host it on ec2 and then how to setup webhook for that