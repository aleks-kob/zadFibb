FROM python:alpine
WORKDIR /Users/supciola/Desktop
COPY main.py main.py
CMD [ "python", "./main.py" ]