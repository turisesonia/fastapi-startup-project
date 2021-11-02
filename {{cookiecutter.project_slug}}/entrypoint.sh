#!/bin/bash

case $1 in
"web")
    echo "Run web api"
    python -m uvicorn app.main:app --proxy-headers --host 0.0.0.0 $2 $3 $4
    ;;
"worker")
    echo "Run celery worker"
    python -m celery -A app.tasks.parser worker --loglevel=INFO --concurrency=1 -Q $2 -n $3
    ;;
"flower")
    echo "Run celery flower monitor"
    python -m celery -A app.tasks.parser flower
    ;;
*)
    echo "Not support case $1"
    ;;
esac
