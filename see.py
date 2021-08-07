""" Module to see all of the database """

from mysql.connector import connect, Error
from colr import color


def see():
    try:
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="app_list"
        )
        cur = conn.cursor()
        query = """ SELECT * FROM app_list """
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print("\n")
            print(
                color(" [*] ID » ", fore="#3c565b"), color(str(row[0]), fore="#7fa5a4")
            )
            print(
                color(" [*] NAME » ", fore="#3c565b"),
                color(str(row[1]), fore="#7fa5a4"),
            )
            print(
                color(" [*] TYPE » ", fore="#3c565b"),
                color(str(row[2]), fore="#7fa5a4"),
            )
            print(
                color(" [*] DESCRIPTION » ", fore="#3c565b"),
                color(str(row[3]), fore="#7fa5a4"),
            )
            print(
                color(" [*] LINK » ", fore="#3c565b"),
                color(str(row[4]), fore="#fbf3a6"),
            )
            print("\n")
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    see()
