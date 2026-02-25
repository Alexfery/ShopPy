from django.shortcuts import get_object_or_404, redirect, render
from catalog.models import Product
from .cart import Cart
from .forms import CartUpdateForm

def detail(request):
    breadcrumbs = [{"label": "Acasă", "url": "/"}, {"label": "Coș"}]
    return render(request, "cart/detail.html", {
        "meta_title": "Coș — Tablouri din licheni",
        "meta_description": "Revizuiește produsele din coș și continuă către checkout.",
        "breadcrumbs": breadcrumbs,
    })

def add(request, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, is_active=True)
    if request.method == "POST":
        qty = int(request.POST.get("quantity", 1))
        cart.add(product, quantity=qty, update_quantity=False)
    return redirect("cart:detail")

def remove(request, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:detail")

def update(request, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id, is_active=True)
    if request.method == "POST":
        form = CartUpdateForm(request.POST)
        if form.is_valid():
            cart.add(product, quantity=form.cleaned_data["quantity"], update_quantity=True)
    return redirect("cart:detail")
