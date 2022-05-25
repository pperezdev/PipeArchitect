FROM python:3.8
FROM node:14-alpine AS development

WORKDIR /tmp

COPY . /tmp

ARG env_flask_variable_web=main.py 

ENV FLASK_APP=$env_flask_variable_web 
ENV NODE_ENV development

COPY package.json .
COPY yarn.lock .
RUN yarn install

CMD [ "yarn", "start" ]
RUN pip install -r requirements.txt