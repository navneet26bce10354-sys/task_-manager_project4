file_name = "tasks_data.txt"

def save_task(task):
    file = open(file_name, "a")
    file.write(task + "\n")
    file.close()

def get_tasks():
    try:
        file = open(file_name, "r")
        tasks = file.readlines()
        file.close()
        return tasks
    except:
        return []
