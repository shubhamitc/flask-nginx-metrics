FROM python:2.7
LABEL maintainer="shubhamkr619@gmail.com"
ENV PYTHONUNBUFFERED=0

COPY . /

RUN pip install -r requirements.txt 

ENTRYPOINT ["python","-u","health.py"]