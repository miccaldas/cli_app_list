""" Searches the database by type of app """
from mysql.connector import connect, Error
import questionary
from questionary import Style
from colr import color


def type_list():
    """Connects to the db and gets a updated list of types"""
    try:
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="app_list"
        )
        cur = conn.cursor()
        lista_de_tipos = []
        query = "SELECT type FROM app_list"
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            lista_de_tipos.append(row)
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    lista_de_tipos = set(
        lista_de_tipos
    )  # https://www.geeksforgeeks.org/python-set-method/
    lst_type = []
    for i in lista_de_tipos:
        lst_type.append(i[0])
    return lst_type


if __name__ == "__main__":
    type_list()


def questionary_types():
    app_style = Style(
        [
            ("qmark", "fg:#117576 bold"),  # token in front of the question
            ("question", "fg:#0f9a99 bold"),  # question text
            ("answer", "fg:#f4deb8 bold"),  # submitted answer text behind the question
            (
                "pointer",
                "fg:#6d7b8d bold",
            ),  # pointer used in select and checkbox prompts
            (
                "highlighted",
                "fg:#f0512a bold",
            ),  # pointed-at choice in select and checkbox prompts
            ("separator", "fg:#dddddd"),  # separator in lists
            ("text", "#ebf4fa"),  # plain text
        ]
    )

    question = questionary.select(
        "What are you looking for?",
        choices=type_list(),
        qmark=" ",
        style=app_style,
        use_indicator=True,
    )
    questionary_types.tpquest = question.ask()  # https://tinyurl.com/yh8jjz98


if __name__ == "__main__":
    questionary_types()


def database_query():
    try:
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="app_list"
        )
        cur = conn.cursor()
        query = (
            "SELECT * FROM app_list WHERE type = '"
            + str(questionary_types.tpquest)
            + "'"
        )
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
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
                color(str(row[4]), fore="#6d7b8d"),
            )
            print("\n")
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    database_query()
