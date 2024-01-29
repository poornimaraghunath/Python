# In this project will integrate Github with Jira which helps the developers to track the issues created in github.
   
      This project helps the developer to reduce the time spending on jira backlog creation because in this project when developer sees the issues created in github he can comment there only which can create jira backlog without logging into the jira.

#This feature will help when the QA team or any other team when working the github if they any find any bugs in the code they will create issue so developer once in a week or 2 days will login the github and check the issues . IIn that case of the issue is not valid they can close the issue there only  but if the issue is valid they need to work on it and track the time spent on it for that developer needs to spend time on creating jora backlog.

#For this developers has seeked the help from the devops team to automate this process 

#In this proccess github and jira are two resources need to interact  so for interaction will use python as bridge between them.

#In this if any comments /jira on the issue it will trigger the webhooks on github and provides the information about the issue to the python application deployed on Ec2.Github will provide the information in the form of json data to python application and then python application makes an api call to jira to cretae the backlog

#In this will learn how to create  jira backlog how to use jira apps and then how to write the python application using flask.

#Then will learn how to convert python application for flask and then how to host it on ec2 and then how to setup webhook for that

# steps involved in this project
  
  1. Jira account creation
  2. Jira api calls
  3. python app cration
  4. python script execution 

# We need to interact with jira through API to make API call we need to generate API token.

# How to create API token in jira 

1. Go to profile 
2. Manage your account
3. Security 
4. API Token : ATATT3xFfGF0esGjRq5zNl1NI1VRVkeqGlyJF770cg1Ae3qjjhHf0vwlgpKAzFiune5G8k3p2tdE845gK3ayZ9vj2nq8wOynYdGe4DWt-BPaCZNBXOHfvY5Hy6qdp9ez8udiK5WDRhgUfVOTw94uVqT2NbpsMeo5vSBZxeFvrEIzP4ubhOK7A5Q=C0C6943C

# Use this document for jira API 
https://developer.atlassian.com/cloud/jira/software/rest/intro/#introduction

# We can list the projects created on jira dash board using an API by writing the program(link to list the projects)
https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-rest-api-3-project-get

Never forget to enter the email id and API token