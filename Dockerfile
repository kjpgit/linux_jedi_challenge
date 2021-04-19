FROM public.ecr.aws/ubuntu/ubuntu:18.04

RUN apt-get update && apt-get install -y python3

ENV LANG=C.UTF-8

WORKDIR /root/

COPY .profile /root/
COPY game.py /usr/bin/
RUN chmod +x /usr/bin/game.py

ENTRYPOINT /bin/bash --login
