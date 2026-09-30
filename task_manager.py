import file_handler
import validation

def add_task():
    print("\n--- Add Task ---")
    name = input("Enter task: ")
    subject = input("Enter subject: ")

    print("1. Pending")
    print("2. Done")
    choice = input("Enter status: ")

    if validation.check_status(choice) == False:
        print("Invalid status")
        return

    if choice == "1":
        status = "Pending"
    else:
        status = "Done"

    task = name + "," + subject + "," + status
    file_handler.save_task(task)
    print("Task added")

def show_tasks():
    tasks = file_handler.get_tasks()

    if len(tasks) == 0:
        print("No tasks found")
        return

    print("\n--- Tasks ---")
    for task in tasks:
        data = task.strip().split(",")
        print("Task:", data[0], "| Subject:", data[1], "| Status:", data[2])
