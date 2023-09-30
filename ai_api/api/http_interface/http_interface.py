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

    def send_prompt(self, prompt):
        self.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        response = api_communication.post_gpt(self.model, self.messages)

        if response.ok:
            response_data = response.json()
            message = response_data["choices"][0]["message"]

            self.messages.append(message)
            utils.save_message(message)

            return message
        else:
            raise Exception(f"Api Exception {response.status_code}")


