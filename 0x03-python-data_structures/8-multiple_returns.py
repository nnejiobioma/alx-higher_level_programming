#!/usr/bin/python3
def multiple_returns(sentence):
    max = (len(sentence), sentence[0] if len(sentence) > 0 else None)
    return max
