from django.shortcuts import render
from .models import Author

# Create your views here.


def index(request):

    list = Author.objects.all()
    text = {'list': list}
    return render(request, 'news/index.html', text)
