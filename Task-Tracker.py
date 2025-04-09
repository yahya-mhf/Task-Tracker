from datetime import datetime
import json

class Task:
    def __init__(self, ID, description, status, createdAT, updatedAT):
        self.ID = ID
        self.description = description
        self.status = status
        self.createdAT = createdAT
        self.updatedAT = updatedAT

    def to_dict(self):
        return {
            'ID' : self.ID,
            'description' : self.description,
            'status' : self.status,
            'createdAT' : self.createdAT,
            'updatedAT' : self.updatedAT
        }


# add Task
# update task
# delete

# list all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

def Add_Task(stock):

    print(f"Add Task :")

    ID = int(input("ID : "))
    description = input("description : ")
    status = "Todo"
    createdAT = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # updatedAT = input("updatedAT : ") to add in update function

    t = Task(ID, description, status, createdAT, None)

    stock[f"Task{len(stock)}"] = t.to_dict()
    save(stock)

def save(stock):
    with open('Tasks.json', 'a', encoding='utf-8') as f:
        json.dump(stock, f, ensure_ascii=False, indent=4)



def list_All_Tasks(stock):

    if len(stock) == 0:
        print("there is no Tasks for the moment")
    with open('Tasks.json', 'r', encoding='utf-8') as f:
        show = json.load(f)
        print(show)






def main():
    stock = dict()
    #t = Task(len(stock), "description", "status", "createdAT", "updatedAT")

    Add_Task(stock)
    list_All_Tasks(stock)



if __name__=="__main__":
    main()
