"""Main module of the app, where all functionalities meet"""

from __future__ import unicode_literals
import sys
import questionary
from questionary import Style
from add import add
from delete import delete
from search import search
from srch_type import type_list, questionary_types, database_query
from update import update
from see import see

app_style = Style(
    [
        ("qmark", "fg:#3c565b bold"),  # token in front of the question
        ("question", "fg:#3c565b bold"),  # question text
        ("answer", "fg:#f4deb8 bold"),  # submitted answer text behind the question
        ("pointer", "fg:#6d7b8d bold"),  # pointer used in select and checkbox prompts
        (
            "highlighted",
            "fg:#f0512a bold",
        ),  # pointed-at choice in select and checkbox prompts
        ("separator", "fg:#dddddd"),  # separator in lists
        ("text", "#dddddd"),  # plain text
    ]
)

print("\n")
resposta = questionary.select(
    "What do you want to do?",
    choices=[
        "Add an Entry",
        "Search by Keyword",
        "Search by Type",
        "See All",
        "Update an Entry",
        "Delete an Entry",
        "Exit",
    ],
    qmark=" ",
    style=app_style,
    use_indicator=True,
).ask()

if resposta == "Add an Entry":
    add()
if resposta == "Search by Keyword":
    search()
if resposta == "Search by Type":
    type_list()
    questionary_types()
    database_query()
if resposta == "See All":
    see()
if resposta == "Update an Entry":
    update()
if resposta == "Delete an Entry":
    delete()
if resposta == "Exit":
    sys.exit()
