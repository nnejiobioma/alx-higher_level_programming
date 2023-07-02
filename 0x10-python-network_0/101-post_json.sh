#!/bin/bash
# JSON task that sends a POST request and displayed body of the response
curl -s -d @"$2" -X POST -H "Content-Type: application/json" "$1"
