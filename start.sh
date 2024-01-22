docker build -t fastapi-app .
docker run -p 8000:8000 -e OPENAI_API_KEY="your_openai_api_key" fastapi-app
