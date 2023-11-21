#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cursor = db.cursor()
    query = """
            SELECT cities.name FROM
            cities INNER JOIN states ON states.id=cities.state_id
            WHERE states.name=%s
            """
    cursor.execute(query, (argv[4], ))
    cities = [row[0] for row in cursor.fetchall()]
    print(*cities, sep=", ") 
    cursor.close()
    db.close()  
