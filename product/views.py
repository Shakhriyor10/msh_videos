from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def home(request):
    categories = Category.objects.all()
    selected_category_id = request.GET.get("category")
    show_all_categories = request.GET.get("show_all") == "1"
    products = (
        Product.objects.select_related()
        .prefetch_related("categories", "tags")
        .all()
    )
    if selected_category_id:
        products = products.filter(categories__id=selected_category_id)
    hot_products = products.filter(is_hot=True)[:4]
    return render(
        request,
        "product/home.html",
        {
            "products": products,
            "hot_products": hot_products,
            "categories": categories,
            "featured_categories": categories[:8],
            "show_all_categories": show_all_categories,
            "selected_category": categories.filter(
                pk=selected_category_id
            ).first(),
        },
    )


def product_detail(request, pk: int):
    product = get_object_or_404(
        Product.objects.prefetch_related("categories", "tags"),
        pk=pk,
    )
    similar_products = (
        Product.objects.prefetch_related("categories", "tags")
        .filter(tags__in=product.tags.all())
        .exclude(pk=product.pk)
        .distinct()[:4]
    )
    return render(
        request,
        "product/detail.html",
        {"product": product, "similar_products": similar_products},
    )
