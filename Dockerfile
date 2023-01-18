FROM python:3.10

ADD . /code
WORKDIR /code

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

CMD python3.10 app.py