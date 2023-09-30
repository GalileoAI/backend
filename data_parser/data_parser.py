import json


class DataParser:
    before_questionare_path = "data/before_questionare.json"
    after_questionare_path = "data/after_questionare.json"

    @classmethod
    def GetBeforeQuestionare(self) -> str:
        questionare_str: str
        with open(self.before_questionare_path, "r") as questioare:
            questionare_str = json.load(questioare)
            questionare_str = json.dumps(questionare_str, indent=4)
            questioare.close()

        return questionare_str
    
    @classmethod
    def GetAfterQuestionare(self) -> str:
        questionare_str: str
        with open(self.after_questionare_path, "r") as questioare:
            questionare_str = json.load(questioare)
            questionare_str = json.dumps(questionare_str, indent=4)
            questioare.close()

        return questionare_str
