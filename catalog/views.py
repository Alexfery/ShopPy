from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Category, Product

SORT_OPTIONS = {
    "newest": "-created_at",
    "price_asc": "price",
    "price_desc": "-price",
}

def product_list(request):
    qs = Product.objects.filter(is_active=True).select_related("category")

    category_slug = request.GET.get("category", "").strip()
    if category_slug:
        qs = qs.filter(category__slug=category_slug)

    q = request.GET.get("q", "").strip()
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))

    sort = request.GET.get("sort", "newest")
    qs = qs.order_by(SORT_OPTIONS.get(sort, "-created_at"))

    paginator = Paginator(qs, 9)
    page_obj = paginator.get_page(request.GET.get("page"))

    categories = Category.objects.all()

    breadcrumbs = [
        {"label": "Acasă", "url": "/"},
        {"label": "Catalog"},
    ]

    return render(request, "catalog/product_list.html", {
        "categories": categories,
        "page_obj": page_obj,
        "category_slug": category_slug,
        "sort": sort,
        "q": q,
        "meta_title": "Catalog — Tablouri din licheni",
        "meta_description": "Explorează colecția noastră de tablouri din licheni stabilizați (moss art).",
        "breadcrumbs": breadcrumbs,
    })

def product_detail(request, slug: str):
    product = get_object_or_404(Product.objects.select_related("category"), slug=slug, is_active=True)

    breadcrumbs = [
        {"label": "Acasă", "url": "/"},
        {"label": "Catalog", "url": "/catalog/"},
        {"label": product.category.name, "url": product.category.get_absolute_url()},
        {"label": product.name},
    ]

    return render(request, "catalog/product_detail.html", {
        "product": product,
        "meta_title": f"{product.name} — Tablouri din licheni",
        "meta_description": (product.description[:150] + "...") if product.description else "Tablou din licheni stabilizați — premium, eco, handmade.",
        "breadcrumbs": breadcrumbs,
    })
