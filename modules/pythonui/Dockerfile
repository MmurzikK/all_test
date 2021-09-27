FROM python:3.8.5-buster

WORKDIR /opt

COPY requirements.txt requirements.txt

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y \
    default-jdk \
    wget \
    unzip \
    dpkg\
    python-pytest \
    && pip install -r requirements.txt \
    && wget -O allure.zip https://github.com/allure-framework/allure2/releases/download/2.14.0/allure-2.14.0.zip \
    && unzip allure.zip -d /opt/allure \
    && rm allure.zip \
    && ln -s /opt/allure/allure-2.14.0/bin/allure /usr/bin/allure 
    

COPY server.py server.py

CMD python -m server.py