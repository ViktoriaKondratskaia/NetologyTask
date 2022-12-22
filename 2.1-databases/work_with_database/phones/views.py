from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    all_phones = Phone.objects.all()
    sort_pages = request.GET.get('sort', '')

    if sort_pages == 'max_price':
        phones = all_phones.order_by('-price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort_pages == 'min_price':
        phones = all_phones.order_by('price')
        context = {'phones': phones}
        return render(request, template, context)

    elif sort_pages == 'name':
        phones = all_phones.order_by('name')
        context = {'phones': phones}
        return render(request, template, context)

    context = {'phones': all_phones}
    return render(request, template, context)




def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
