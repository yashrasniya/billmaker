from django.shortcuts import render,redirect
from .models import data
from .forms import data_of_user


# Create your views here.
def index(request):
    number = 3
    number=request.POST.get('num',True)

    form = data_of_user(request.POST or None)
    if form.is_valid():
        form.save();
        form = data_of_user()
        return redirect('product')
    lis=[]
    for a in range(int(number)):
        lis.append(a)
    context = {
        'form': form,
        'num':lis
    }
    return render(request, 'index.html', context)
