FROM python:2.7
LABEL maintainer="shubhamkr619@gmail.com"

COPY . /
ENV FLASK_APP=hello.py

RUN pip install -r requirements.txt 
EXPOSE 8080

ENTRYPOINT ["python", "-m", "flask", "run" ,"--port=8080", "-h", "0.0.0.0"]