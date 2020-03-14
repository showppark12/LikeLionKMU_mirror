FROM python:3.7
ENV PYTHONUNBUFFERED 1

# backend 디렉토리를 추가.
WORKDIR /app/backend

COPY ./KMU_likelion/requirements.txt /app/backend
RUN pip3 install --upgrade pip -r requirements.txt

COPY ./KMU_likelion/ /app/backend
