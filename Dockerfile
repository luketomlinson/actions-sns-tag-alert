FROM python:3.8-slim-buster

RUN apt-get update \
 && apt-get install -y git

RUN pip install --no-cache-dir -U pip wheel

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app
COPY ~/.gitconfig $HOME

ENTRYPOINT ["/app/action.py"]
