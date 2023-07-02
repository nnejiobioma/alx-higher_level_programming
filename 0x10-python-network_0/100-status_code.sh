#!/bin/bash
# Sends a request to URL and displays reaponse
curl -s "$1" -L -X HEAD -w "%{http_code}"
