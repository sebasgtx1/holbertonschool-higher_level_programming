#!/usr/bin/python3
""" script that takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument
"""
if __name__ == "__main__":
    import sys
    import MySQLdb
    mydb = MySQLdb.connect(host="localhost",
                           port=3306, user=sys.argv[1],
                           password=sys.argv[2],
                           database=sys.argv[3])
    mycursor = mydb.cursor()
    q = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
            ORDER BY id ASC".format(sys.argv[4])
    mycursor.execute(q)
    myresult = mycursor.fetchall()
    for row in myresult:
        print(row)
    mycursor.close()
    mydb.close()
