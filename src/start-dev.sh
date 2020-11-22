#!/usr/bin/env bash
set -e -o pipefail

uvicorn main:app --host 0.0.0.0 --port 5001 --no-access-log --reload
