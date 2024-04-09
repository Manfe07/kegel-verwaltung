#!/bin/sh

gunicorn --worker-class eventlet -w 1 -b :8000 app:app --access-logfile ./logs/log.txt --log-level debug 