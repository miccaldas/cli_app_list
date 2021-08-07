""" Module to search the database """

from mysql.connector import connect, Error
from colr import color


def search():
    try:
        print("\n")
        busca = input(color(" What are you searching for? ", fore="#3c565b"))
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="app_list"
        )
        cur = conn.cursor()
        query = (
            " SELECT * FROM app_list WHERE MATCH(name, type, description) AGAINST ('"
            + busca
            + "' IN NATURAL LANGUAGE MODE)"
        )
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print("\n")
            print(
                color(" [*] ID » ", fore="#3c565b"), color(str(row[0]), fore="#6d7b8d")
            )
            print(
                color(" [*] NAME » ", fore="#3c565b"),
                color(str(row[1]), fore="#6d7b8d"),
            )
            print(
                color(" [*] TYPE » ", fore="#3c565b"),
                color(str(row[2]), fore="#6d7b8d"),
            )
            print(
                color(" [*] DESCRIPTION » ", fore="#3c565b"),
                color(str(row[3]), fore="#6d7b8d"),
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
    search()
