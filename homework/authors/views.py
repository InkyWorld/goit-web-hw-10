from django.shortcuts import render
from bson import ObjectId

from homework.utils.mongo_connection import connect_mongo


def author(request, id_):
    db = connect_mongo().authors
    author = db.find_one({"_id" : ObjectId(id_)})

    return render(
        request,
        "authors/author.html",
        context={'author': author},
    )