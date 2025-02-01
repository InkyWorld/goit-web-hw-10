import json

from bson import ObjectId
from mongo_connection import connect

db = connect()

with open("authors.json", encoding="UTF-8") as fd:
    authors = json.load(fd)

for author in authors:
    # Document to insert
    # Insert if not exists
    db.authors.update_one(
        {"fullname": author["fullname"]},  # Query to find document
        {"$setOnInsert": author},  # Only insert if not found
        upsert=True,
    )

with open("quotes.json", encoding="UTF-8") as fd:
    quotes = json.load(fd)

for quote in quotes:
    # Document to insert
    # Insert if not exists
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        document = {
            'quote' : quote['quote'],
            'author' : author['_id'],
            'tags' : quote['tags'] 
        }
        db.quotes.update_one(
            {"quote": quote["quote"]},  # Query to find document
            {"$setOnInsert": document},  # Only insert if not found
            upsert=True,
        )