# Read the JSON file using json package and place the data in a class instaces
# The file is in the /resources/ folder and is called RATP.json

import json

from dataclasses import dataclass
FILE_PATH = "resources/users.json"

@dataclass
class User:
    id: int
    name: str
    city: str
    school: str
    age: int
    is_teacher: bool

def read_json(file_path: str) -> list[User]:
    users = []
    with open(file_path) as json_file:
        data = json.load(json_file)
        for user in data:
            user = User(
                id=int(user["id"]),
                name=user["name"],
                city=user["city"],
                school=user["school"],
                age=int(user["age"]),
                is_teacher=user["is_teacher"]
            )
            users.append(user)
    return users

users = read_json(FILE_PATH)
print(users[0])