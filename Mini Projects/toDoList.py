def addTasks():
    newTask=input("Enter a task you want to add:")
    tasks.append(newTask)

def removeTasks():
    task=input("Enter the task you want to remove:")
    found=False
    for i in range(len(tasks)):
        if tasks[i].lower()==task.lower():
            taskRemoved=tasks.pop(i)
            print(f"task : {taskRemoved} is removed")
            found=True
            break
    if not found:
        print((f"task: {task} not found in your list"))

    # if task in tasks:
    #     tasks.remove(task)
    #     print(f"task => {task} is removed")
    # else:
    #     print(f"task: {task} not found in your list")

def showTasks():
    if tasks:
        print("Your pending tasks:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("No task found in your list!!!!!!")

tasks=[]

while True:
    print("TO DO LIST")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show the tasks")
    print("4. Exit")
    print("Enter your choice:")
    choice=int(input("Enter what you want to perform:"))
    if(choice==1):
        addTasks()
    elif(choice==2):
        removeTasks()
    elif(choice==3):
        showTasks()
    elif(choice==4):
        break
    else:
        print("invalid choice")