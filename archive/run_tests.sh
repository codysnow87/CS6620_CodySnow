#!/bin/sh
# script must be run from the directory containing this script
# build the Docker image
docker build -t flask-api-tests .
# run the Docker container
docker run --rm -p 8080:5000 flask-api-tests