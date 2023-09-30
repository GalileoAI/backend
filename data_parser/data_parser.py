import json


class DataParser:
    questionare_base_path = "data/"
    questionare_file_name = "_questionare.json"

    @classmethod
    def GetQuestionare(self, qkey: str) -> str:
        questionare_str: str
        questionare_file_path = self.questionare_base_path + qkey + self.questionare_file_name

        with open(questionare_file_path , "r") as questioare:
            questionare_str = json.load(questioare)
            questionare_str = json.dumps(questionare_str, indent=4)
            questioare.close()

        return questionare_str
    
    # @classmethod
    # def AnswersToPrompt(seld, answers: str):

print(DataParser.GetQuestionare("before"))