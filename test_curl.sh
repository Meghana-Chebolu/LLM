'''
Note: The URL in the curl command i.e,'https://8000-meghanachebolu-llm-p3qbcm1t19p.ws-us107.gitpod.io/get_chatGPT_completion'
      is dynamic.It changes everytime we create a new environment in Gitpod.
How to get your CURL command?
Once you build and run your Docker application, open the application and open docs by appending the application URL with '/docs'.
Click on any of the methods say POST /get_chatgpt_completition.Try it out and execute it.You will get the curl command.
Now you can use the curl command and test the API from the terminal.

'''
# Example of my CURL command to test ChatGPT API
curl -X 'POST' \
  'https://8000-meghanachebolu-llm-p3qbcm1t19p.ws-us107.gitpod.io/get_chatGPT_completion' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'chatgpt_api_key=xyzxyz&prompt=What%20is%20a%20haiku%3F' 
# Example of my CURL command to test Gemini API
curl -X 'POST' \
  'https://8000-meghanachebolu-llm-p3qbcm1t19p.ws-us107.gitpod.io/get_gemini_completion' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'gemini_api_key=xyzxyz&prompt=What%20is%20a%20haiku%3F'
# Example of my CURL command to test LLaMA Replicate API
curl -X 'POST' \
  'https://8000-meghanachebolu-llm-p3qbcm1t19p.ws-us107.gitpod.io/get_replicate_completion' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'replicate_key=abcd&system_prompt=Be%20kind&prompt=What%20is%20a%20haiku%3F'

