from dataclasses import asdict
from type_definitions import School, SchoolDescription, Recommendation, UserResponse

import json
import re


class DataParser:
    questionare_base_path = "data/"
    questionare_file_name = "_questionare.json"

    @classmethod
    def GetQuestionare(self, qkey: str) -> str:
        questionare_str: str
        questionare_file_path = self.questionare_base_path + qkey + self.questionare_file_name

        with open(questionare_file_path , "r") as questioare:
            questionare_json = json.load(questioare)
            questionare_str = json.dumps(questionare_json, indent=4)
            questioare.close()

        return questionare_str
    
    @classmethod
    def AnswersToPrompt(self, answers: str) -> str: 
        ai_query = ""
        questionare_with_answers = json.loads(answers)

        if "questions" in questionare_with_answers:
            result_list = questionare_with_answers["questions"]

            for result in result_list:
                ai_query = ai_query + "Question " + result["id"] + ": " + result["question_str"] + "\n"
                ai_query = ai_query + "Answer to question " + result["id"] + ": " + result["answer_str"] + "\n"

        return ai_query

    @classmethod
    def GetPositionsList(self, ai_response: str) -> [str]:
        positions = []
        
        # input_str = ""
        # with open("data_parser/DirtyOutput.txt") as input:
        #     input_str = input.read()
        #     input.close()
        # input_str = input_str[input_str.find(":\n") + 1:]

        for line in ai_response.splitlines():
            result = re.split(":", line)
            position_str = result[0][3:]
            if len(position_str) > 0:
                positions.append(position_str)

        return positions[:-1]

    @classmethod
    def GetScoolsList(self, ai_response: str) -> [School]:
        # university_response = ""
        school_list = []
        index = 0

        # with open("data_parser/UniversitiesExample.txt") as uni_file:
        #     university_response = uni_file.read()
        #     uni_file.close()

        for line in ai_response.splitlines():
            school_name_match = re.match(r"[0-9](.*)", line)
            faculty_match = re.match(r"   - Faculty: ", line)
            website_match = re.match(r"   - Website: ", line)

            if school_name_match:
                school_list.append(School(line[3:], SchoolDescription("", "")))

            if faculty_match:
                school_list[index].description.faculty = line[14:]

            if website_match:
                school_list[index].description.website = line[14:]
                index = index + 1

        return school_list
                
    @classmethod
    def CreateRecommendation(self, position: str, school_list: School) -> Recommendation:
        return Recommendation(position, school_list)
    
    @classmethod
    def CreateResponse(self, recommendations: [Recommendation]) -> str:
        user_output = UserResponse("recommendation", recommendations)
        json_output = json.dumps(asdict(user_output), indent=4)

        return json_output

# print(DataParser.CreateResponse([DataParser.CreateRecommendation("Elektryk", DataParser.GetScoolsList(""))]))
print(DataParser.GetPositionsList(""));