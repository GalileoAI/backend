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