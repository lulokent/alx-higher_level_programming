#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0-usa wherename matches the argument.
"""
import sys
import MySQLdb


if __name__ = "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3],
                           port=3306)
    cur = conn.cursor()
    quer = sys.argv[4]
    cur.execute("""SELECT * FROM states WHERE name LIKE %s;""", (quer, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
