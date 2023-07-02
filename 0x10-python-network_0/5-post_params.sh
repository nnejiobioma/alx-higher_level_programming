#!/bin/bash
# Takes in URL sends POST request, displays response
curl -s -X POST -d "$1" "email=test@gmail.com&subject=I will always be here for PLD"
