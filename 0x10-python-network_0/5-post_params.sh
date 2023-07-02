#!/bin/bash
# Takes in URL sends POST request, displays response
curl -s -d -X POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
