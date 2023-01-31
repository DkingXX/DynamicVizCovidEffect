FROM python:3.8-slim AS build

RUN apt-get update \
  && apt-get install gcc make -y \
  && apt-get clean

# set working directory
RUN mkdir -p /app
WORKDIR /app

# add requirements
COPY . /app

# install requirements
RUN pip install -r requirements.txt

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
RUN mkdir -p /app
WORKDIR /app

COPY --from=build /app /app
COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
# run server
CMD ["./entrypoint.sh"]
