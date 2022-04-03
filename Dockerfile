FROM ubuntu:18.04
USER root

WORKDIR /App

RUN apt-get update
RUN apt-get install -y git python3 python3-pip
RUN pip3 install boto3 botocore Flask PyJWT python-dotenv

COPY . .

ENTRYPOINT ["/App/run.sh"]
