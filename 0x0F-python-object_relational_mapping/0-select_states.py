#!/usr/bin/python3
# lists all states from the database hbtn_0e_0_usa
# Your script should take 3 arguments:
#  < mysql username >, < mysql password > and < database name >


import MySQLdb
import sys

if __name__ == "__main__":
    # check if the correct number of arguments is 4
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states`")

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
