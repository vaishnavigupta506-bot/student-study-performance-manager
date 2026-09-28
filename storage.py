import json
import os


DATA_FILE = "data.json"


def load_all_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)

                if isinstance(data, list):
                    return {
                        "tasks": data,
                        "marks": {},
                        "profile": {}
                    }

                return data

        except json.JSONDecodeError:
            return {}

    return {}


def save_tasks(tasks):
    data = load_all_data()
    data["tasks"] = tasks

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_tasks():
    data = load_all_data()
    return data.get("tasks", [])


def save_profile(name, registration_number, branch):
    data = load_all_data()

    data["profile"] = {
        "name": name,
        "registration_number": registration_number,
        "branch": branch
    }

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_profile():
    data = load_all_data()
    return data.get("profile", {})


def save_marks(marks):
    data = load_all_data()
    data["marks"] = marks

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_marks():
    data = load_all_data()
    return data.get("marks", {})