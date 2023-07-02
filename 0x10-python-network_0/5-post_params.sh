#!/bin/bash
# Takes in URL sends POST request, displays response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
