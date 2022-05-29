from django.shortcuts import render
from products.forms import SearchProduct
from products.models import Product
from django.views.decorators.http import require_http_methods


def home(request):

    return render(request, "products/home.html")


@require_http_methods(['POST'])
def search_product(request):
    form = SearchProduct(request.POST)
    if form.is_valid():
        product_user = form.cleaned_data
        product_wanted = product_user['product']
        product_db = Product.objects.filter(name__icontains=product_wanted)
        return render(request, "products/products.html", context={"products": product_db})


def food(request, product_id):
    product_detail = Product.objects.get(id=product_id)
    return render(request, "products/food.html", context={"product": product_detail})

