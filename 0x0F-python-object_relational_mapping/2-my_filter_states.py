#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the state table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = db_connect(
            host="localhost",
            port=3306,
            user=argv[1],
            pword=argv[2],
            db=argv[3]
            )
    db_cursor = db_connect.cursor()

    db_cursor.execute("SELCT * FROM states WHERE name LIKE BINARY '{}' ORDER BY \ states.id ASC".format(argv[4]))
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

    db_cursor.close()
    db_connect.close()
