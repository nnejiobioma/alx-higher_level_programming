#!/bin/bash
# Takes in URL sends POST request, displays response
curl -sd -X POST  "email=test@gmail.com&subject=I will always be here for PLD" "$1"
