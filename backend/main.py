from fastapi import FastAPI, HTTPException, Query,Form
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
import openai
import google.generativeai as genai

app = FastAPI()

# adding cors urls
origins=[
    'http://localhost',
    'http://localhost:3000',
    'https://*.gitpod.io',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/bot_query")
def bot_query(input_text: str):
    return {"output_text": input_text.lower()}

@app.post("/get_chatGPT_completion")
async def get_chatGPT_completion(
    api_key: str =Form(...),
    prompt: str  =Form(...),  
):
    try:
        openai.api_key = api_key  # Set the API key
        model: str = "gpt-3.5-turbo"
        temperature: float = 0
        max_tokens: int = 256
        top_p: float = 1
        frequency_penalty: float = 0.0
        presence_penalty: float = 0.0

        messages = [{"role": "user", "content": prompt}]

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
        )

        resp = response['choices'][0]['message']['content']
        return {"response": resp}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))