# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JBrecht,8.5.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
import os.path
from os import path
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
if path.exists(objFile):
    objFile = open(objFile, "r")
    for row in objFile:
        t, p = row.split(",")  # Returns a list!
        dicRow = {"Task": t.strip(), "Priority": p.strip()}
        lstTable.append(dicRow)
    print(lstTable)
    objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new task
    3) Remove an existing task
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task | Priority")
        for row in lstTable:
            print(row["Task"], " | ", row["Priority"], sep="")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        lstTable.append({"Task": input("Enter task name: "), "Priority": input("Enter task priority: ")})
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strData = (input("Enter name of task to remove: "))
        for row in lstTable:
            if row["Task"].lower() == strData.lower():
                lstTable.remove(row)
                print(strData + " removed")
                print(lstTable)
            else:
                print(strData + " not found")
                print(lstTable)
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"] + "\n"))
        objFile.close()
        print("Now in file!")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Goodbye")
        break  # and Exit the program
