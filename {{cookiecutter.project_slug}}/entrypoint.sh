#!/bin/bash

case $1 in
"fastapi")
    echo "Run FastAPI backend application"
    uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 80 --forwarded-allow-ips "*" ${@:2}
    ;;

"typer")
    echo "Run Typer command line application"
    python -m app.typer ${@:2}
    ;;

*)
    echo "Not support case $1"
    ;;
esac

