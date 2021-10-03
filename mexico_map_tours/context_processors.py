import json
from estados import models
def base(request):
    with open('estados/static/estados/estados.json', encoding='utf-8') as json_file: 
        estados_list = json.load(json_file)

    
    categories = models.category_list
    return {
        'estados_list': estados_list,
        'categories': categories
    }