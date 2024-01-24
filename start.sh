#Docker commands
docker build -t llm .
docker run -p 8000:8000 llm

#Git 
git add .
git commit -m ""
git push

# run from command line
uvicorn main:app --host 0.0.0.0 --port 8000 --reload