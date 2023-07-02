#!/bin/bash
#this script takes, URL and sends URL.
curl -s "$1" | wc -c
