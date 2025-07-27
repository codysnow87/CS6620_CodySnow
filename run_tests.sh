#!/bin/sh
COMPOSE_FILE="docker-compose.yml"

docker compose -f "$COMPOSE_FILE" --profile test up --build --abort-on-container-exit --exit-code-from test-runner

EXIT_CODE=$?
if [ $EXIT_CODE -ne 0 ]; then
    echo "Tests failed with exit code $EXIT_CODE"
else
    echo "Tests passed successfully"
fi

docker compose -f "$COMPOSE_FILE" --profile test down --volumes