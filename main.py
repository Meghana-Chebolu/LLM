from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import os
import openai
import google.generativeai as genai

app = FastAPI()

# Retrieve the OpenAI API key from the command line or use an empty string if not provided
openai.api_key = os.getenv("OPENAI_API_KEY", default="")
class ChatGPTRequest(BaseModel):
    model: str = "gpt-3.5-turbo"
    prompt: str = "print hello world!"
    temperature: float = 0
    max_tokens: int = 256
    top_p: float = 1
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
@app.post("/get_chatGPT_completion")
def get_chatGPT_completion(chat_request: ChatGPTRequest):
    try:
        messages = [{"role": "user", "content": chat_request.prompt}]

        response = openai.ChatCompletion.create(
            model=chat_request.model,
            messages=messages,
            temperature=chat_request.temperature,
            max_tokens=chat_request.max_tokens,
            top_p=chat_request.top_p,
            presence_penalty=chat_request.presence_penalty,
            frequency_penalty=chat_request.frequency_penalty,
        )

        resp = response['choices'][0]['message']['content']
        return {"response": resp}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return response


if __name__ == "__main__":
    import uvicorn

    # Get the OpenAI API key from the command line
    openai.api_key = input("Enter your OpenAI API Key: ")

    uvicorn.run(app, host="127.0.0.1", port=8000)
