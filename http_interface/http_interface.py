from . import api_communication
from . import utils


class GPTClient:
    def __init__(self, model: str, system_prompt: str):
        self.model = model
        self.messages = [
            {
                "role": "system",
                "content": system_prompt
            },
        ]
        utils.save_message(self.messages[-1], initialized=True)

    def jobs_by_questionare(self, questionare) -> str:
        self.send_prompt("system", f"Remember the answers given by the student on this questionare: {questionare}")
        self.send_prompt("system", "You give a json string as an answer where every position has name and description")
        jobs = self.send_prompt("user", "What 5 jobs would be the most suitable for the student?")
        jobs.replace("\n", "")
        return jobs

    def schools_by_job(self, job):
        self.send_prompt("system", f"Answer all questions based on this career path chosen by the student: {job}")
        self.send_prompt("system", "You give a json string as an answer where every position has name and description")
        schools = self.send_prompt("user", "What are the 5 best universities in Poland that offer faculties related to this career path")
        return schools

    def send_prompt(self, role, prompt):
        self.messages.append(
            {
                "role": role,
                "content": prompt
            }
        )

        response = api_communication.post_gpt(self.model, self.messages)

        if response.ok:
            response_data = response.json()
            message = response_data["choices"][0]["message"]

            self.messages.append(message)
            utils.save_message(message)

            return message["content"]
        else:
            raise Exception(f"Api Exception {response.status_code}")




