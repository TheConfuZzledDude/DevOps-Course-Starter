FROM python:3.11 as base
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry/ python3 -
RUN mkdir /app
WORKDIR /app
COPY pyproject.toml poetry.toml poetry.lock ./
RUN /etc/poetry/bin/poetry install
COPY todo_app/ todo_app/
ENTRYPOINT ["/etc/poetry/bin/poetry", "run"]

FROM base as production
EXPOSE 80/tcp
CMD ["gunicorn", "--bind", "0.0.0.0:80", "todo_app.app:create_app()"]

FROM base as development
EXPOSE 5000/tcp
CMD ["flask", "run", "--host", "0.0.0.0"]
