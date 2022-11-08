from django.shortcuts import render
from app.models import UserPage


# Create your views here.


def index_page(request):
    userpages = UserPage.objects.all()
    context = {
        "userpages": userpages
    }
    return render(request, 'app/index.html', context)
