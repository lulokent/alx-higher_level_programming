#!/usr/bin/python3
"""
Lists all states with name starting with N from the database
hbtn_0e_0_usa sorted in ascending order by states.id
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQldb.connect(host="localhost", port=3306,
                            user=sys.argv[1], password=argv[2],
                            db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'"" ORDER BY states.id ASC;""")
    rows = cursor.fetchall()
    for row in rows:
        print (row)
    cur.close()
    conn.close()
