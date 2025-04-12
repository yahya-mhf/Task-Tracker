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
    return {}


def writefile (data):
    with open('Tasks.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return True


def Mess_with_data(argument, ID, name, Newname, status):
    # Read data from the file
    data = readfile()


    New_data = data

    if argument == 'Add_Task':
        New_data = Add_Task(name, data)

    elif argument == 'Update_Task':
        New_data = Update_Task(ID, Newname, data)

    elif argument == 'Delete_Task':
        New_data = Delete_Task(ID, data)

    elif argument == 'Mark_Task':
        New_data = Mark_task (ID, status, data)

    # Sava tha changed informations
    writefile (New_data)
    return New_data


###########################################
def Add_Task(name, data, status = 'Todo'):
    #remove the updete function
    print(f"Task name : {name}")

    updatedAT = "Not updated"


    if data:
        existing_iDs = []
        for key in list(data.keys()):
            existing_iDs.append(int(key.split()[0][4:]))
        existing_iDs.sort()
        ID = existing_iDs[-1] + 1
    else:
        ID = 0


    print(f"Task ID : {ID}")
    description = input("description : ")
    createdAT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    New_task = {'ID' : ID ,
                'description' : description,
                 'status' : status,
                 'createdAT' : createdAT,
                 'updatedAT' : updatedAT
                }

    data[f"Task{ID} : {name}"] = New_task

    return data
##################################################################################################################

def Update_Task(ID, Newname, data):
    # make it independent
    prefix = f"Task{ID}"
    for key in list(data.keys()):
        if key.startswith(prefix):
            task = data[key]
            task['description'] = input("description : ")
            task['updatedAT'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            new_key = f"Task{ID} : {Newname}"
            data[new_key] = task
            del data[key]
            break

    return data

def Delete_Task(ID, data):
    prefix = f"Task{ID}"
    for key in list(data.keys()):
        if key.startswith(prefix):
            del data[key]
            break
    return data


def Mark_task (ID, status, data):
    prefix = f"Task{ID}"
    for key in data:
        if key.startswith(prefix):
            data[key]['status'] = status[5:]
            data[key]['updatedAT'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            break
    return data
###################################################################################################################


def list_All_Tasks():

    data = readfile()
    if data:
        for key, value in data.items():
            print(f"{key} : ")
            for k , v in value.items():
                print(f"{k} : {v}")
            print("")
    else:
        print("there is no Task for the moment")

def List_By_Status(desired_status):
    data = readfile()
    if data:
        for key, value in data.items():
            if value['status'] == desired_status:
                print(f"{key} : ")
                for k , v in value.items():
                    print(f"{k} : {v}")
                print("")
    else:
        print(f"no Task is in {desired_status}")



def main():

    #t = Task(len(stock), "description", "status", "createdAT", "updatedAT")
    if len(argv) == 3 and argv[1] == 'add':
        Mess_with_data('Add_Task', None, argv[2], None, None)

    elif len(argv) == 4 and argv[1] == 'update' :
        Mess_with_data('Update_Task', argv[2], None, argv[3], None)

    elif len(argv) == 3 and argv[1] == 'delete':
        Mess_with_data('Delete_Task', argv[2], None, None, None)

    elif len(argv) == 3 and argv[1][:4] == 'mark':
        Mess_with_data('Mark_Task', argv[2], None, None, argv[1])


    elif len(argv) == 2 and argv[1] == 'list':
        list_All_Tasks()

    elif len(argv) == 2 and (argv[1] == 'list-in-progress' or argv[1] == 'list-done' or argv[1] == 'list-todo'):
        List_By_Status(argv[1][5:])

    else :
        print("""
    Usage:
    python main.py add "TaskName"
    python main.py update ID "NewTaskName"
    python main.py delete ID
    python main.py markDone ID
    python main.py markInProgress ID
    python main.py list
    python main.py list-status Todo|Done|InProgress
""")


if __name__=="__main__":
    main()
