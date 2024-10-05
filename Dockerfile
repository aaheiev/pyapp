ARG PYTHON_VERSION=3.12.7-alpine3.20

FROM python:${PYTHON_VERSION}

ARG POETRY_VERSION="1.8.3"
ENV POETRY_HOME="/opt/poetry"
ENV PATH="${POETRY_HOME}/bin:${PATH}"
COPY ./pyproject.toml ./poetry.lock*  ./

RUN pip install poetry \
    && poetry config virtualenvs.create false
RUN poetry install --no-root --no-dev

COPY ./app /app

ENV USER=app
ENV GROUPNAME=$USER
ENV UID=1001
ENV GID=1001

RUN addgroup --gid "$GID" "$GROUPNAME" \
    &&  adduser \
      --disabled-password \
      --gecos "" \
      --home /app \
      --ingroup "$GROUPNAME" \
      --no-create-home \
      --uid "$UID" \
      $USER \
    && chown -R $USER:$GROUPNAME /app

USER $USER

WORKDIR /app
