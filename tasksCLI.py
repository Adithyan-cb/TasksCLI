#!/usr/bin/env python3
import json
import sys
from datetime import datetime
import argparse
import os
import uuid

FILEPATH = '/home/adithyan/Adithyan/projects/mini-projects/tasks.json'


# function to get all task from task.json
def getTask(filename:str):
    if os.path.exists(filename):
        try:
            with open(filename,'r')as file:
                tasks = json.load(file)
        except json.JSONDecodeError:
            tasks=[]
    else:
        tasks=[]

    return tasks


        
# fucntion to add new task
def addTask(task:str):
    # generate unique ID for each task
    ID = str(uuid.uuid4())[:4]
    createdAt = datetime.now()
    data={
            "id":ID,
            "describtion":task,
            "status":"todo",
            "createdAt":createdAt.strftime("%d-%m-%y | %H:%M"),
            "updatedAt":createdAt.strftime("%d-%m-%y | %H:%M")   
        }

    task = getTask(FILEPATH)

    task.append(data)

    with open(FILEPATH,'w')as file:
        json.dump(task,file,indent=4)
        

    print(f"task added successfully | ID:{ID}")


# function to list tasks based on status
def displayTasks(status:str):

    tasks = getTask(FILEPATH)

    if status == 'todo':
        for i in range(len(tasks)):
            if tasks[i]['status'] == 'todo':
                print("====================")
                print(f"ID : {tasks[i]['id']}")
                print(f"description : {tasks[i]['describtion']}")
                print(f"status : {tasks[i]['status']}")
                print(f"created at : {tasks[i]['createdAt']}")
                print(f"updated at : {tasks[i]['updatedAt']}")
                print("=====================\n")
    elif status == 'in-progress':
        for i in range(len(tasks)):
            if tasks[i]['status'] == 'in-progress':
                    print("====================")
                    print(f"ID : {tasks[i]['id']}")
                    print(f"description : {tasks[i]['describtion']}")
                    print(f"status : {tasks[i]['status']}")
                    print(f"created at : {tasks[i]['createdAt']}")
                    print(f"updated at : {tasks[i]['updatedAt']}")
                    print("=====================\n")
    elif status == 'done':
         for i in range(len(tasks)):
            if tasks[i]['status'] == 'done':
                    print("====================")
                    print(f"ID : {tasks[i]['id']}")
                    print(f"description : {tasks[i]['describtion']}")
                    print(f"status : {tasks[i]['status']}")
                    print(f"created at : {tasks[i]['createdAt']}")
                    print(f"updated at : {tasks[i]['updatedAt']}")
                    print("=====================\n")
    else:
        for i in range(len(tasks)):
            print("====================")
            print(f"ID : {tasks[i]['id']}")
            print(f"description : {tasks[i]['describtion']}")
            print(f"status : {tasks[i]['status']}")
            print(f"created at : {tasks[i]['createdAt']}")
            print(f"updated at : {tasks[i]['updatedAt']}")
            print("=====================\n")            
        
    
        

# function to update a task
def updateTask(ID:str,newDesc:str):

    tasks = getTask(FILEPATH)
    flag =0
    newUpdatedAt = datetime.now()
    for i in range(len(tasks)):
        if ID == tasks[i]['id']:
            tasks[i]['describtion'] = newDesc
            tasks[i]['updatedAt'] = newUpdatedAt.strftime("%d-%m-%y | %H:%M")
            print(f"task with id:{ID} updated successfully.")
            flag=1

    if not flag:
        print("ID does not exists.")
            
            
    with open(FILEPATH,'w')as file:
        json.dump(tasks,file,indent=4)

# function to delete a task
def deleteTask(ID:str):

    tasks = getTask(FILEPATH)
    isDeleted=0

    for i in range(len(tasks)):

        if ID == tasks[i]['id']:
            tasks.pop(i)
            isDeleted=1
            print(f"task with id:{ID} deleted.")

    if not isDeleted:
        print("invalid id or task with the id does not exist.")

    with open(FILEPATH,'w')as file:
        json.dump(tasks,file,indent=4)    
        
# function to update status of the task
def statusUpdater(ID:str,status:str):
    tasks = getTask(FILEPATH)
    doesExists=0
    for i in range(len(tasks)):

        if ID == tasks[i]['id']:
            tasks[i]['status'] = status
            doesExists=1
            print(f"status changed to {status}")

    if not doesExists:
        print("invalid id or task does not exists.")

    with open(FILEPATH,'w')as file:
        json.dump(tasks,file,indent=4)
    

# main function
def main():    
    parser = argparse.ArgumentParser(prog="tasksCLI")
    subparsers = parser.add_subparsers(dest="tag", help="Command to run")
    
    # command to add a new task
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("task", type=str, help="The task description")

    # command to update the describtion of a task
    parser_update = subparsers.add_parser("update",help="update the task")
    parser_update.add_argument("ID",type=str,help="ID of the task that you want to update")
    parser_update.add_argument("describtion",type=str,help="new desription for the task")

    # command to delete a task
    parser_delete = subparsers.add_parser("delete",help="used to delete a task")
    parser_delete.add_argument("ID",type=str,help="ID of the task what you wan to delete")

    # command to change status to 'in-progress'
    parser_mark_inProgress = subparsers.add_parser("mark-in-progress",help="change the status of task to 'in-progress'")
    parser_mark_inProgress.add_argument("ID",type=str,help="ID of the task")

    # command to change status to 'done'
    parser_mark_done = subparsers.add_parser("mark-done",help="changes status of the task to 'done'")
    parser_mark_done.add_argument("ID",type=str,help="ID of the task")
    
    # list command with optional arguments [todo,in-progress,done]
    parser_list = subparsers.add_parser("list", help="List all tasks")
    parser_list.add_argument(
        "status", 
        nargs="?", 
        choices=["done", "todo", "in-progress"], 
        help="Optional: filter tasks by status"
    )
    

    args = parser.parse_args()
    
    match args.tag:
        case "add":
            addTask(args.task)
        case "list":
            if args.status == 'todo':
                displayTasks('todo')
            elif args.status == 'in-progress':
                displayTasks('in-progress')
            elif args.status == 'done':
                displayTasks('done')
            else:
                displayTasks('all')
            
        case "update":
            updateTask(args.ID,args.describtion)
        case "delete":
            deleteTask(args.ID)
        case "mark-in-progress":
            statusUpdater(args.ID,'in-progress')
        case "mark-done":
            statusUpdater(args.ID,'done')
        case _:
            parser.print_help()


# calling main function
main()
