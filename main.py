import task_manager
import analysis

def menu():
    while True:
        print("\n=== TASK MANAGER ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task_manager.add_task()
        elif choice == "2":
            task_manager.show_tasks()
        elif choice == "3":
            analysis.show_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

menu()
