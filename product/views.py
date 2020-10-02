from django.shortcuts import render,redirect
from .models import product
from .forms import product_details
# Create your views here.
def product(requst):
    form = product_details(requst.POST or None)
    if form.is_valid():
        form.save();
        form = product_details()
        return redirect('/')

    data={
        'form':form,

    }
    return render(requst,'product.html',data)
