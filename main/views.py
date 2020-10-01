from django.shortcuts import render
from .models import data
from .forms import data_of_user


# Create your views here.
def index(request):
    form = data_of_user(request.POST or None)
    if form.is_valid():
        form.save()
        form = data_of_user()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)
