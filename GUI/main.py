from tkinter import *

# Refresh Function which refreshes the listbox after clicking any button 
def refresh_listbox():
     listbox.delete(0,END)
     with open ("tasks.txt","r") as f:
        tasks = f.readlines()
        for task in tasks:
            listbox.insert(END,task.strip())

# Adds to the file.txt then to listbox
def add():
    
        with open ("tasks.txt","a") as f:
            task = entry.get()
            if task != "":
                f.write(entry.get() + "\n")
                entry.delete(0, END)
                print("Task added!")
            else:    
                print("You havent assigned the task!")
        refresh_listbox()

#Removes any task from listbox    
def remove():
    # Get the selected task
    selected = listbox.curselection()

    if not selected:
        print("Please select a task.")
        return

    task_to_remove = listbox.get(selected)

    # Read all tasks
    with open("tasks.txt", "r") as f:
        tasks = f.readlines()

    # Remove the selected task
    new_tasks = []

    for task in tasks:
        if task.strip() != task_to_remove:
            new_tasks.append(task)

    # Write the updated tasks back
    with open("tasks.txt", "w") as f:
        f.writelines(new_tasks)

    # Clear the Entry
    entry.delete(0, END)

    # Refresh the Listbox
    refresh_listbox()

    print("Task removed!")
        
        

# Refreshes the listbox if there is any problem
def refresh():
            refresh_listbox()

# deletes all the task present in listbox
def delete():
     with open("tasks.txt","w") as f :
          f.write("")
          refresh_listbox()

window = Tk()
window.title("To Do List App")

icon = PhotoImage(file="python.png")
window.iconphoto(True,icon)

#Entry box
entry = Entry(window,
              font=("Impact",70),
              bg="black",
              fg="#00FF00")
entry.pack(side=TOP,padx=10,pady=10)


#Add button
add_button = Button(window,
                    text="Add",
                    font=("Impact",20),
                    command=add)
add_button.pack(side=RIGHT)

#Remove button   

remove_button = Button(window,
                    text="Remove",
                    font=("Impact",20),
                    command=remove)
remove_button.pack(side=RIGHT)

# Refresh button 
refresh_button = Button(window,
                    text="refresh",
                    font=("Impact",20),
                    command=refresh)
refresh_button.pack(side=RIGHT)

#Delete button
delete = Button(window,
                text="Delete all task",
                font=("Impact",20),
                command=delete)
delete.pack(side=RIGHT)

# Listbox where task would be showed
listbox = Listbox(window,
                  font=("Impact",20))
refresh_listbox()

listbox.pack(side=BOTTOM)


window.mainloop()

