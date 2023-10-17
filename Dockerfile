FROM python:3.11.6-slim-bullseye

WORKDIR /app

RUN apt-get update

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip

# Install Poetry and project dependencies
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY . /app/

ENTRYPOINT [ "poetry", "run", "python" ]

CMD ["app.py"]