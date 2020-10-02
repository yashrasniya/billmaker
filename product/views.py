from django.shortcuts import render,redirect
from .models import product
from .forms import product_details
# Create your views here.
def product(requst):
    # number = requst.POST.get('num', True)

    form = product_details(requst.POST or None)
    name = requst.POST.get('name_of_product', True)
    print(name,"hii")
    if form.is_valid():
        form.save()
        form = product_details()
        return redirect('/')
    if requst.POST.get('num',True) is not None:
        number=requst.POST.get('num',True)

        lis=[]
        for a in range(int(number)):
            lis.append(a)
        data = {
            'form': form,
            'num': lis
        }

        return render(requst,'product.html',data)
    # lis = []
    # for a in range(int(number)):
    #     lis.append(a)
    data = {
        'form': form,
        # 'num': lis
    }
    return render(requst,'product.html',data)
