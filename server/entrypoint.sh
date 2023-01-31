#!/usr/bin/env sh

# start server
uvicorn --host '0.0.0.0' --port 7001 --log-level info main:app
