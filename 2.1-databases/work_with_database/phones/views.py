from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_catalog = request.GET.get('sort')
    template = 'catalog.html'
    
    phones = Phone.objects.all()

    if sort_catalog == 'name':
        phones = phones.order_by('name')
    elif sort_catalog == 'min_price':
        phones = phones.order_by('price')
    elif sort_catalog == 'max_price':
        phones = phones.order_by('-price')

    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {
        'phone': phone,
    }
    return render(request, template, context)
