#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    mydb = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           password=sys.argv[2], database=sys.argv[3])
    mycursor = mydb.cursor()
    q = "SELECT cities.id, cities.name, states.name FROM states\
        LEFT JOIN cities ON states.id = cities.state_id ORDER BY cities.id ASC"
    mycursor.execute(q)
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
    mycursor.close()
    mydb.close()
