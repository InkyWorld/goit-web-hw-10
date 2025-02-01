from django import template
from bson import ObjectId

from homework.utils.mongo_connection import connect_mongo

register = template.Library()

@register.filter(name='author')
def get_author(id_):
    db = connect_mongo()
    author = db.authors.find_one({'_id': ObjectId(id_)})
    return author['fullname']
