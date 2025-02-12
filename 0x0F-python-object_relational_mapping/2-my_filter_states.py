#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the state table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb as db
from sys import argv


if __name__ = "__main__":
    conn = db.conn(host="localhost",
                   port=3306,
                   user=argv[1],
                   password=argv[2],
                   db=argv[3]
                   )
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
            ORDER BY states.id ASC""".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
