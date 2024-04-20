#!/usr/bin/python3
"""
Lists all states with name starting with N (upper N) from the database
hbtn_0e_0_usa sorted in ascending order by states.id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1],
                           password=sys.argv[2],
                           db=sys.argv[3])
    # create a cursor for the connection
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%'"" ORDER BY states.id")
    # Fetch the results
    rows = cursor.fetchall()
    # iterate through list
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
