""" Module to delete apps from the database """

from mysql.connector import connect, Error
from colr import color


def delete():
    print("\n")
    ident = input(color(" ID to delete? » ", fore="#3c565b"))

    try:
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="app_list"
        )
        cur = conn.cursor()
        query = " DELETE FROM app_list WHERE id = " + ident
        cur.execute(query)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    delete()
