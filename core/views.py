from django.shortcuts import render_to_response
from core import models
 
def index(request): #Define our function, accept a request
    items = models.todo.objects.all() #ORM queries the database for all of the to-do entries.
    return render_to_response('index.html', {'items': items}) 