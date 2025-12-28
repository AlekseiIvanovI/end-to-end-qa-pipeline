#!/bin/bash

echo "Running API Load Test with Newman..."

# Install newman and HTML reporter if not present
npm install -g newman newman-reporter-htmlextra

# Run load test: 500 virtual users, 30s ramp-up, 60s duration
newman run collections/REQRES_API_Load_Test.postman_collection.json \
  -e environments/REQRES_Env.postman_environment.json \
  --reporters cli,htmlextra \
  --reporter-htmlextra-export reports/load-test-report.html \
  --iteration-count 500 \
  --delay-request 100