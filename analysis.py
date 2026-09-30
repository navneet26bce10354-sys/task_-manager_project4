import file_handler

def show_summary():
    tasks = file_handler.get_tasks()
    total = 0
    pending = 0
    done = 0

    for task in tasks:
        data = task.strip().split(",")
        if len(data) >= 3:
            total = total + 1
            if data[2] == "Pending":
                pending = pending + 1
            else:
                done = done + 1

    print("\n--- Summary ---")
    print("Total:", total)
    print("Pending:", pending)
    print("Done:", done)
