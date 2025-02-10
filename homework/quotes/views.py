from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from . import forms
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
        context={"quotes": quotes_on_page},
    )


@login_required
def add_quote(request):
    if request.method == "POST":
        form = forms.QuoteForm(request.POST)
        if form.is_valid():
            db_authors = connect_mongo().authors
            db_quotes = connect_mongo().quotes

            quote = form.cleaned_data["quote"]
            fullname = form.cleaned_data["author"]
            tags = request.POST.getlist('tags')
            clear_tags = []
            for tag in tags:
                if tag.strip():
                    clear_tags.append(tag.strip())

            author_id = db_authors.find_one({"fullname": fullname}).get('_id')
            if author_id:
                document = {
                    "quote": quote,
                    "author": author_id,
                    "tags": clear_tags,
                }
                db_quotes.update_one(
                    {"quote": quote},
                    {"$setOnInsert": document},
                    upsert=True,
                )
                messages.success(request, f"Вітаємо автор {fullname} успішно створений або оновлений")
            else:
                messages.error(request, f"Автор {fullname} не знайдений")

    form = forms.QuoteForm()
    return render(request, "quotes/add_quote.html", context={"form": form})



@login_required
def add_author(request):
    if request.method == "POST":
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            db = connect_mongo().authors
            fullname = form.cleaned_data["fullname"]
            document = {
                "fullname": fullname,
                "born_date": form.cleaned_data["born_date"].strftime("%B %d, %Y"),
                "born_location": form.cleaned_data["born_location"],
                "description": form.cleaned_data["description"],
            }
            db.update_one(
                {"fullname": fullname},
                {"$setOnInsert": document},
                upsert=True,
            )
            messages.success(request, f"Вітаємо автор {fullname} успішно створений або оновлений")
    
    form = forms.AuthorForm()
    return render(request, "quotes/add_author.html", context={"form": form})
