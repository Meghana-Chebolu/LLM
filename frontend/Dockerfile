FROM node:16-alpine3.17

# set working directory
WORKDIR /frontend

# add `/app/node_modules/.bin` to $PATH
ENV PATH /frontend/node_modules/.bin:$PATH

RUN apk add iputils curl

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
# RUN npm install --silent
RUN npm cache clean --force
RUN npm install
RUN npm install react-scripts@5.0.1 -g --silent
RUN npm install react-bootstrap bootstrap 
RUN npm install reactflow
#RUN npm install axios  # Add this line to install Axios
RUN npx update-browserslist-db@latest
RUN npm install webpack-dev-server@latest --save-dev
RUN npm install webpack-dev-middleware --save-dev

# add app
COPY . ./

EXPOSE 3000

ENV REACT_APP_BACKEND_URL=https://8000-meghanachebolu-llm-7bg3igl9sz1.ws-us107.gitpod.io

# start app
CMD ["npm", "start"]