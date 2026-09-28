from marks import marks_manager
from tasks import task_manager
from report import performance_report
from storage import save_profile, load_profile, load_tasks


def student_profile():
    print("\n========== STUDENT PROFILE ==========")

    name = input("Enter your name: ")
    registration_number = input("Enter your registration number: ")
    branch = input("Enter your branch: ")

    print("\n---------- STUDENT PROFILE ----------")
    print("Name:", name)
    print("Registration Number:", registration_number)
    print("Branch:", branch)

    print("\nProfile created successfully!")

    save_profile(name, registration_number, branch)

    return name, registration_number, branch


def main():

    print("========================================")
    print(" STUDENT STUDY & PERFORMANCE MANAGER")
    print("========================================")

    # Load saved student profile
    profile = load_profile()

    name = profile.get("name", "Not Available")
    registration_number = profile.get(
        "registration_number", "Not Available"
    )
    branch = profile.get("branch", "Not Available")

    # Load saved tasks
    tasks = load_tasks()

    # Marks will be handled by Marks Manager
    marks = {}

    while True:

        print("\n========== MAIN MENU ==========")
        print("1. Student Profile")
        print("2. Marks Manager")
        print("3. Study Task Manager")
        print("4. Performance Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            name, registration_number, branch = student_profile()

        elif choice == "2":

            marks = marks_manager()

        elif choice == "3":

            tasks = task_manager()

        elif choice == "4":

            performance_report(
                name,
                branch,
                marks,
                tasks
            )

        elif choice == "5":

            print(
                "\nThank you for using the "
                "Student Study & Performance Manager!"
            )

            print("Goodbye!")
            break

        else:

            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()