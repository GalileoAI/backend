from dataclasses import dataclass, asdict
import json


@dataclass
class Question:
    id: str
    question_str: str
    answer_str: str    

@dataclass
class Questionare:
    header: str
    questions: list[Question]

@dataclass
class SchoolDescription:
    faculty: str
    website: str

@dataclass
class School:
    name: str
    description: SchoolDescription

@dataclass
class Recommendation:
    position: str
    schools: list[School]

@dataclass
class UserResponse:
    header: str
    positions: list[Recommendation]

# u_resp = UserResponse("recommendation", [Recommendation("Engineer", [School("UMK", SchoolDescription("faculty1", "www."))]), Recommendation("Budowlaniec", [School("Technikum budowlane", SchoolDescription("faculty1", "www.123"))])])
# ur_json = json.dumps(asdict(u_resp), indent=4)
# print(ur_json)

# json_str = "{\"position\": [\"abc\", \"def\"]}"
# new_json = json.loads(json_str)
# print(new_json["position"][0])