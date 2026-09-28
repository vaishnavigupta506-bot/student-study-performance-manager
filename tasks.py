from storage import save_tasks, load_tasks


def task_manager():
    tasks = load_tasks()

    while True:
        print("\n========== STUDY TASK MANAGER ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            subject = input("Enter subject: ")

            task_data = {
                "task": task,
                "subject": subject,
                "status": "Pending"
            }

            tasks.append(task_data)
            save_tasks(tasks)

            print("Task added successfully!")

        elif choice == "2":
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                print("\n---------- YOUR TASKS ----------")

                for i, task in enumerate(tasks, start=1):
                    print("\nTask", i)
                    print("Description:", task["task"])
                    print("Subject:", task["subject"])
                    print("Status:", task["status"])

        elif choice == "3":
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                print("\nSelect a task to complete:")

                for i, task in enumerate(tasks, start=1):
                    print(i, ".", task["task"])

                try:
                    task_number = int(input("Enter task number: "))

                    if 1 <= task_number <= len(tasks):
                        tasks[task_number - 1]["status"] = "Completed"
                        save_tasks(tasks)
                        print("Task marked as completed!")
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                print("\nSelect a task to delete:")

                for i, task in enumerate(tasks, start=1):
                    print(i, ".", task["task"])

                try:
                    task_number = int(input("Enter task number: "))

                    if 1 <= task_number <= len(tasks):
                        deleted_task = tasks.pop(task_number - 1)
                        save_tasks(tasks)
                        print("Deleted:", deleted_task["task"])
                    else:
                        print("Invalid task number.")

                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            print("Leaving Study Task Manager...")
            return tasks

        else:
            print("Invalid choice. Please select 1-5.")