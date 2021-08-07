""" Module to add apps to the db """

from mysql.connector import connect, Error
from colr import color


def add():
    """Prompts the user for the information and sends it to the db"""
    print("\n")
    nome = input(color(" Name? » ", fore="#3c565b"))
    tipo = input(color(" Type? » ", fore="#3c565b"))
    descrição = input(color(" Description » ", fore="#3c565b"))
    linque = input(color(" Link » ", fore="#3c565b"))

    answers = [nome, tipo, descrição, linque]

    try:
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="app_list"
        )
        cur = conn.cursor()
        query = """ INSERT INTO app_list (name, type, description, link) VALUES (%s, %s, %s, %s) """
        cur.execute(query, answers)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    add()
