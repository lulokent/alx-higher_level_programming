#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_usa sorted in ascending
order by states.id.
"""
import MySqldb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], password=sys.argv[2],
                           db=sys.argv[3])
    # create a cursor
    cur=conn.cursor()
    # execute MySQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch results
    rows = cur.fetchall()
    # Loop through results
    for row in rows:
        print (row)
    # close cursor
    cur.close()
    conn.close()
