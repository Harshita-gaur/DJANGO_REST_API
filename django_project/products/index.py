from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product
@register(Product) #similar to admin
class ProductIndex(AlgoliaIndex):
    # should_index = 'is_public'
    fields = [
        'title',
        # 'content',
        'body',
        'price',
        'user',
        'public',
        'path',
#         'endpoint',
    ]
    settings = {
        'searchableAttributes': ['title', 'body'],
        'attributesForFaceting': ['user', 'public']
    }
    tags = 'get_tags_list'