import json  

def save():
    with open("tasks.json", "w") as f:
        json.dump(task, f)


def load():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


task = load() 


def add():
    while True:
        x = input("Enter task: ").strip()

        if x == "":
            print("Error: Task is empty")
        elif x.isdigit():
            print("Error: Task cannot be only numbers")
        else:
            task.append({"title": x, "done": False})
            save()  # NEW
            print("Task added successfully!")
            break


def show():
    if not task:
        print("No tasks found")
        return

    for i in range(len(task)):
        print(i, task[i]["title"], task[i]["done"])


def complete():
    if not task:
        print("No tasks found")
        return

    show()

    try:
        n = int(input("Which task number to finish? "))

        if 0 <= n < len(task):
            task[n]["done"] = True
            save()  # NEW
            print("Task completed!")
        else:
            print("Invalid task number")

    except ValueError:
        print("Please enter a valid number")


def delete():
    if not task:
        print("No tasks found")
        return

    show()

    try:
        x = int(input("Which task number to delete? "))

        if 0 <= x < len(task):
            removed = task.pop(x)
            save()  # NEW
            print("Deleted:", removed["title"])
        else:
            print("Invalid task number")

    except ValueError:
        print("Please enter a valid number")


def delete_all():
    if not task:
        print("No tasks to delete")
    else:
        task.clear()
        save()  # NEW
        print("All tasks deleted!")


def search():
    if not task:
        print("No tasks found")
        return

    l = input("What word do you want to search? ").strip().lower()

    if not l:
        print("Please enter a search word")
        return

    found = False

    for i in task:
        if l in i["title"].lower():
            status = "Done" if i["done"] else "Not done"
            print(i["title"], "-", status)
            found = True

    if not found:
        print("No matching tasks found")


while True:
    print("\n1: Add")
    print("2: Show")
    print("3: Complete")
    print("4: Delete")
    print("5: Delete all")
    print("6: Search")
    print("7: Exit")

    choice = input("Choose a number (1-7): ")

    if choice == "1":
        add()
    elif choice == "2":
        show()
    elif choice == "3":
        complete()
    elif choice == "4":
        delete()
    elif choice == "5":
        delete_all()
    elif choice == "6":
        search()
    elif choice == "7":
        print("Exited the program.")
        break
    else:
        print("Invalid choice. Please choose 1-7")