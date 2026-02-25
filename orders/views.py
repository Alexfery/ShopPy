from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem

@require_http_methods(["GET", "POST"])
def checkout(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect("cart:detail")

    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = cart.get_total_price()
            order.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    quantity=item["quantity"],
                    unit_price=item["unit_price"],
                )
                p = item["product"]
                if p.stock >= item["quantity"]:
                    p.stock -= item["quantity"]
                    p.save(update_fields=["stock"])

            cart.clear()
            return redirect("orders:thank_you", order_id=order.id)
    else:
        form = OrderCreateForm()

    breadcrumbs = [{"label": "Acasă", "url": "/"}, {"label": "Coș", "url": "/cart/"}, {"label": "Checkout"}]

    return render(request, "orders/checkout.html", {
        "form": form,
        "meta_title": "Checkout — Tablouri din licheni",
        "meta_description": "Finalizează comanda rapid: date livrare + confirmare.",
        "breadcrumbs": breadcrumbs,
    })

def thank_you(request, order_id: int):
    breadcrumbs = [{"label": "Acasă", "url": "/"}, {"label": "Mulțumim"}]
    return render(request, "orders/thank_you.html", {
        "order_id": order_id,
        "meta_title": "Mulțumim — Comandă plasată",
        "meta_description": "Comanda ta a fost înregistrată cu succes.",
        "breadcrumbs": breadcrumbs,
    })
