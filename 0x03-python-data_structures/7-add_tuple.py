#!/usr/bin/python3
def add_tuple(tuple_i=(), tuple_j=()):
    i1 = tuple_i[0] if len(tuple_i) >= 1 else 0
    i2 = tuple_i[1] if len(tuple_i) >= 2 else 0
    j1 = tuple_j[0] if len(tuple_j) >= 1 else 0
    j2 = tuple_j[1] if len(tuple_j) >= 2 else 0
    new_t = (i1 + j1, i2 + j2)
    return new_t
