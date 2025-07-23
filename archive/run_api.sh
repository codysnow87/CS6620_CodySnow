#!/bin/sh
# script must be run from the directory containing this script
# cd to the directory containing dockerfile for APIs
cd REST_API
# build the Docker image
docker build -t flask-api .
# run the Docker container
docker run --rm -p 8080:5000 flask-api
# access the API at http://localhost:5000
echo "API is running at http://localhost:5000"
echo "Press [CTRL+C] to stop the server"
# wait indefinitely
tail -f /dev/null