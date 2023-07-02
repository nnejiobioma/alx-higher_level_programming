#!/bin/bash
# Sends a request to URL and displays reaponse
curl -s -o "$1" /dev/null -w "%{http_code}"
