from validation import get_valid_number
from storage import save_marks, load_marks


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def marks_manager():

    print("\n========== MARKS MANAGER ==========")

    marks = {}

    number_of_subjects = int(get_valid_number(
        "Enter number of subjects: ",
        1,
        20
    ))

    for i in range(number_of_subjects):

        subject = input("Enter subject name: ").strip().upper()

        while subject == "":
            print("Subject name cannot be empty.")
            subject = input("Enter subject name: ").strip().upper()

        mark = get_valid_number(
            "Enter marks (0-100): ",
            0,
            100
        )

        marks[subject] = mark

    # Save marks permanently
    save_marks(marks)

    print("\n---------- MARKS ----------")

    total = 0

    for subject, mark in marks.items():
        print(subject, ":", mark)
        total += mark

    percentage = total / number_of_subjects
    grade = calculate_grade(percentage)

    print("\nTotal Marks:", total)
    print("Percentage:", format(percentage, ".2f"), "%")
    print("Grade:", grade)

    return marks