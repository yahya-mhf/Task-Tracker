import os
from datetime import datetime
import json
from sys import argv

# add Task
# update task
# delete

# list all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress
def is_f_exist(filename):
    if os.path.exists(filename):
        return True
    return False


def readfile ():
    if is_f_exist('Tasks.json'):
        with open('Tasks.json', 'r') as f:
            data = json.load(f)
            return data
    return False


def writefile (data):
    with open('Tasks.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return True


def Add_Task(name):
    print(f"Task name : {name}")
    ID = 0

    data = readfile()
    if data:
        ID = len(data)
    else:
        data = dict()


    print(f"Task ID : {ID}")
    description = input("description : ")
    status = "Todo"
    createdAT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # updatedAT = input("updatedAT : ") to add in update function

    New_task = {'ID' : ID , 'description' : description, 'status' : status, 'createdAT' : createdAT, 'updatedAT' : None }

    data[f"Task{ID} : {name}"] = New_task

    writefile (data)

    return ID


def list_All_Tasks():

    data = readfile()
    if data:
        print(data)
    else:
        print("there is no Task for the moment")



def main():

    #t = Task(len(stock), "description", "status", "createdAT", "updatedAT")
    if len(argv) == 3 and argv[1] == 'add':
        Add_Task(argv[2])
    elif len(argv) == 2 and argv[1] == 'list':
        list_All_Tasks()
    else :
        print("Usage ...")


if __name__=="__main__":
    main()
