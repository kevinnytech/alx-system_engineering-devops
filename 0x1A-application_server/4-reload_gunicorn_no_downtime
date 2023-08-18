#!/bin/bash

# Get the PID of Gunicorn master process
PID=$(pgrep -f 'gunicorn --bind')

if [ -z "$PID" ]
then
  echo "Gunicorn is not running."
else
  # Send the HUP signal to Gunicorn
  kill -HUP $PID
  echo "Gunicorn has been gracefully reloaded."
fi

