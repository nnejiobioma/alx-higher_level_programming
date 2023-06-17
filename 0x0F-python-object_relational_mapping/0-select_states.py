#!/usr/bin/python3
"""Code that list all states in the database"""

import MySQLdb
import sys


def list_states(username, password, database):
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()

    if __name__ == "__main__":
        if len(sys.argv) != 4:
            print("Usage: python script.py <username> <password> <database>")
            sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]


list_states(username, password, database)
