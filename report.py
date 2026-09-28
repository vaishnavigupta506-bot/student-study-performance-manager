def performance_report(name, branch, marks, tasks):
    print("\n========== PERFORMANCE REPORT ==========")

    print("\nStudent:", name)
    print("Branch:", branch)

    # Academic performance
    if len(marks) > 0:
        total = 0

        print("\n---------- ACADEMIC PERFORMANCE ----------")

        for subject, mark in marks.items():
            print(subject, ":", mark)
            total += mark

        percentage = total / len(marks)

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        print("\nTotal Marks:", total)
        print("Percentage:", format(percentage, ".2f"), "%")
        print("Grade:", grade)

    else:
        print("\nNo marks available.")

    # Study task performance
    print("\n---------- STUDY TASK PERFORMANCE ----------")

    total_tasks = len(tasks)
    completed_tasks = 0

    for task in tasks:
        if task["status"] == "Completed":
            completed_tasks += 1

    pending_tasks = total_tasks - completed_tasks

    print("Total Tasks:", total_tasks)
    print("Completed Tasks:", completed_tasks)
    print("Pending Tasks:", pending_tasks)

    if total_tasks > 0:
        completion_percentage = (completed_tasks / total_tasks) * 100
        print(
            "Task Completion:",
            format(completion_percentage, ".2f"),
            "%"
        )
    else:
        print("Task Completion: 0.00 %")

    print("\n========================================")