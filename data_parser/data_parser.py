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
    
    @classmethod
    def AnswersToPrompt(self, answers: str) -> str:
        preparation_str = ""
        ai_query = ""
        questionare_with_answers = json.loads(answers)

        if "questions" in questionare_with_answers:
            result_list = questionare_with_answers["questions"]

            for result in result_list:
                ai_query = ai_query + "Question " + result["id"] + ": " + result["question_str"] + "\n"
                ai_query = ai_query + "Answer to question " + result["id"] + ": " + result["answer_str"] + "\n"

        return ai_query
