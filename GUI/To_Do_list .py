# To Do List

tasks = []
print("="*30)
print("      To Do list App ")
print("="*30)

while True:
    print("1.ADD")
    print("2.REMOVE")
    print("3.SHOW")
    print("4.EXIT")

    choice = input("Enter your choice (1:4) :").strip()

    # Add choice
    if(choice == "1"):
        count = input("How many task do you want to add :")
        if count.isdigit():         
            count=int(count)

            for i in range(count):
                task = input(f"Enter task {i+1} :")
                if task:
                    tasks.append(task)
                    with open("tasks.txt", "w") as f:
                        f.write(task + "\n")
                else :
                    print("Empty task skipped")
            print("Task added!\n")
        else:
            print("Please enter a valid number!")
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")

    # Remove
    elif(choice == "2"):
        with open("tasks.txt") as f:
            tasks = f.readlines()
            tasks = [task.strip() for task in tasks]
            remove_task = input("Which task do you want to remove :").strip()
            if not tasks :
                print("No task to remove")
            else:
                if remove_task in tasks:
                    tasks.remove(remove_task)
                    print("Task removed\n")
            
                else:
                    print("Task not found")
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")

    #Show
    elif(choice == "3"):
        with open("tasks.txt") as f:
            tasks = f.readlines()
        if not tasks:
            print("No tasks yet!\n")
        else:
            print("\nYOUR TASKS")
            for number, task in enumerate(tasks):
                print(f"{number+1}.{task}")
                
    #Exit
    elif(choice == "4"):
        print("Exiting the program\n")
        break

    else:
        print("Invalid number\n")


print("="*30)
print("     PROGRAM ENDED")
print("="*30)