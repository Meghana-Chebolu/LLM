from fastapi import FastAPI, HTTPException, Query,Form
from pydantic import BaseModel
import os
import openai
import google.generativeai as genai
import replicate

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.post("/get_chatGPT_completion")
def get_chatGPT_completion(
    chatgpt_api_key: str =Form(...),
    prompt: str = Form(...),  
):
    try:
        openai.api_key = chatgpt_api_key  # Set the API key
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
@app.post("/get_gemini_completion")
def get_gemini_completion(
    gemini_api_key: str =Form(...),
    prompt: str = Form(...),  
):
    try:
        genai.configure(api_key = gemini_api_key)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                candidate_count=1,
                stop_sequences=['space'],
                max_output_tokens=400,
                temperature=0.7)
        )
        return {"response": resp}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

llama2 = "meta/llama-2-13b-chat:f4e2de70d66816a838a89eeeb621910adffb0dd0baba3976c96980970978018d"

def ChatCompletion(prompt, system_prompt=None):
  output = replicate.run(
    llama2,
    input={"system_prompt": system_prompt,
            "prompt": prompt,
            "max_new_tokens":1000}
  )
  return "".join(output)
def get_answer(prompt):
    system_prompt = """
            You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.
Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content.
Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something
 not correct. If you don't know the answer to a question, please don't share false information.
        """
    return ChatCompletion( prompt=prompt, system_prompt=system_prompt)

@app.post("/get_replicate_completion")
def get_replicate_completion(
    replicate_key: str = Form(...),
    prompt: str = Form(...),
):
    try:
        response = get_answer(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


