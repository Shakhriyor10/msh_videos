from django.shortcuts import get_object_or_404, render

from .models import Product


def home(request):
    products = (
        Product.objects.select_related()
        .prefetch_related("categories", "tags")
        .all()
    )
    hot_products = products.filter(is_hot=True)[:4]
    return render(
        request,
        "product/home.html",
        {
            "products": products,
            "hot_products": hot_products,
        },
    )


def product_detail(request, pk: int):
    product = get_object_or_404(
        Product.objects.prefetch_related("categories", "tags"),
        pk=pk,
    )
    return render(
        request,
        "product/detail.html",
        {"product": product},
    )