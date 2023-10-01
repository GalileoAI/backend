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
        self.save_message("system", f"Remember the answers given by the student on this questionare: {questionare}")
        self.save_message("system", "As a content of your message you only give the list, no headers or footers, just the bullet point list without any comments or summaries")
        self.save_message("system", "For every job you give a name, and description after : sign")
        jobs = self.send_prompt("user", "What 5 jobs would be the most suitable for the student?")
        jobs.replace("\n", "")
        return jobs

    def schools_by_job(self, job):
        self.save_message("system", f"Answer all questions based on this career path chosen by the student: {job}")
        self.save_message("system", "Your list is in the following format: <number>. <school name>:\n  - Faculty: <faculty>\n  - Website: <website>. Restrict your output only to one value for 'Faculty' and one value for 'Website")
        schools = self.send_prompt("user", "What are the 3 best universities in Poland that offer faculties related to this career path")
        return schools

    def save_message(self, role, prompt):
        message = {
            "role": role,
            "content": prompt
        }

        self.messages.append(message)
        utils.save_message(message)

    def send_prompt(self, role, prompt):
        self.save_message(role, prompt)

        response = api_communication.post_gpt(self.model, self.messages)

        if response.ok:
            response_data = response.json()
            message = response_data["choices"][0]["message"]
            self.save_message(message["role"], message["content"])
            return message["content"]
        else:
            raise Exception(f"Api Exception {response.status_code}")




