FROM python:3.10-slim
# FROM python:3.10-alpine

########################################
# add a user so we're not running as root
########################################
RUN useradd pythonuser

RUN python -m pip install --no-cache --upgrade --quiet pip poetry

RUN apt-get update
RUN apt-get install -y git
RUN apt-get clean

RUN mkdir -p build/aws_cloudwatch_log_group

WORKDIR /build
ADD aws_cloudwatch_log_group /build/aws_cloudwatch_log_group
COPY poetry.lock .
COPY CHANGELOG.md .
COPY README.md .
COPY pyproject.toml .

RUN mkdir -p /home/pythonuser/
RUN chown pythonuser /home/pythonuser -R
RUN chown pythonuser /build -R

WORKDIR /build/
USER pythonuser

RUN python -m pip install --upgrade /build/
USER root
RUN rm -rf /build/
USER pythonuser

CMD ["python", "-m", "aws_cloudwatch_log_group" ]