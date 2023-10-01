from dataclasses import dataclass


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
