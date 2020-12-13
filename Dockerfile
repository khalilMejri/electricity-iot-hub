FROM python:latest
WORKDIR /iot-hub
COPY . .
RUN pip3 install -r requirements.txt

