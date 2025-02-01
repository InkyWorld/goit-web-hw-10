from django.shortcuts import render
from django.core.paginator import Paginator
from pymongo.collection import Collection

from homework.utils.mongo_connection import connect_mongo


def main(request, page_number=1):
    db = connect_mongo().quotes
    quotes = db.find()
    PAGE_SIZE = 8
    paginator = Paginator(list(quotes), PAGE_SIZE)
    quotes_on_page = paginator.get_page(page_number)
    return render(
        request,
        "quotes/index.html",
        context={'quotes': quotes_on_page},
    )
