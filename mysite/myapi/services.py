from django.db import connection
from contextlib import closing
from collections import OrderedDict
from rest_framework.exceptions import NotFound

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_author_all():
    authors = query_get_author_all()
    items = []
    for data in authors:
        items.append(
            OrderedDict(
                {
                    "id":  data['id'],
                    "first_name": data['first_name'],
                    "last_name": data['last_name'],
                    "age": data['age'],
                }

            )
        )
        return items

def get_author_one(author_id):
    authors = query_get_author_one(author_id)
    return OrderedDict(
        {
            "id": authors['id'],
            "first_name": authors['first_name'],
             "last_name": authors['last_name'],
            "age": authors['age'],
        }
    )

def query_get_author_all():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" SELECT * FROM myapi_author """)
        authors = dictfetchall(cursor)
    return authors

def query_get_author_one(author_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" SELECT * FROM myapi_author WHERE id = s%""" [author_id],)
        authors = dictfetchall(cursor)
    return authors
