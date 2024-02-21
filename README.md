# Python is a static dynamic language using for building web applicatons, to automate regular tasks a

Datatypes 

1. Text type-string (in this the data will always be in single quotes or double quotes)
2. number type - integer(it contains whole,positive ,negative numbers without decimals)
                 floating point number (it contains positive or negative numbers with decimals)


# How to convert the integer into string ?
   
      str(50) - it will consider the output as the string 

# To concatenate one or more string and integer

print("in 20 days" + str(50) + "are minutes") -- In this output there will no space between the strings

# How to add the space between the strings
method 1
Print("20 days are " + str(50) + " are minutes") - add space at the end of the first string and the begining of last spring

method 2
print(f"20 days are {50} minutes") -it is mostly used method ,it works only in the latest version of python that is above python 3

where f - it stands for format


# Variables 
    They are the containers for storing the values
    In the names for the variables are dynamically typed there is no need for defining the type of variables
    The reserved words of python can't be used as names for the variables

# Functions : 
    They are the logical blocks of the code
    They are defined using the kyeword def
    Function always ends with the colon(:) once the function is written we should the call the fumction otherwise no output will be executed
    The parameters can be passed to the function

# Input()
    It is a built in function in python used to provide inputs
    To use it further the value of the function can be assigned to the new variable

    \n = newline character

    eg. User_input = input("hey user,enter the value of number of days\n")
        print(User_input)

# return
     
     it stores output of the function and that can be assigned to other variable

 eg 1.    calculations_to_units = (24 * 60 * 60)
          name_of_unit = "seconds"

          def days_to_units(num_of_days):
          return f"{num_of_days} days are {num_of_days * calculations_to_units} {name_of_unit}"


          my_variable = days_to_units(20)
          print(my_variable)

