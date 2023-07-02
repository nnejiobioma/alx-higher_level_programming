#!/bin/bash
# Sends a request to URL and displays reaponse
curl -s "$1" -o /dev/null "%{http_code}" -w
