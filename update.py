""" Module to update the database entries"""
import time
from mysql.connector import connect, Error
import click
from colr import color


def update():
    print("\n")
    coluna = input(color(" Column? » ", fore="#3c565b"))
    ident = input(color(" ID? » ", fore="#3c565b"))
    print(color(" Write your update", fore="#3c565b"))
    time.sleep(0.3)
    update = click.edit()

    try:
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="app_list"
        )
        cur = conn.cursor()
        query = (
            "UPDATE app_list SET " + coluna + " = '" + update + "' WHERE id = " + ident
        )
        cur.execute(
            query,
        )
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    update()
