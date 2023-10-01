import os
import requests

api_key = "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"
api_url = "https://api.openai.com/v1/chat/completions"


def post_gpt(model, prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": prompt
    }

    response = requests.post(api_url, headers=headers, json=payload)
    return response
