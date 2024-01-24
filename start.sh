 docker build -t fastapi-backend
  .
 docker run -p 8000:8000 fastapi-backend

 docker build -t react-frontend .
 docker run -p 3000:3000 react-frontend

 cd frontend
 npm install
 docker compose build 
 docker compose up