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
