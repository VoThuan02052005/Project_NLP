FROM ubuntu:latest
LABEL authors="vothu"

ENTRYPOINT ["top", "-b"]