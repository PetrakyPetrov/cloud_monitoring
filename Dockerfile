FROM ubuntu:20.04
RUN apt-get update && apt-get install -y build-essential git libjpeg-dev
RUN apt-get install -y vim
RUN apt-get -y install python3
WORKDIR /app
COPY . .
EXPOSE 30001
CMD [ "python3", "main.py"]
