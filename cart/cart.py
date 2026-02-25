from decimal import Decimal
from django.conf import settings
from catalog.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product: Product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "unit_price": str(product.price)}
        if update_quantity:
            self.cart[product_id]["quantity"] = int(quantity)
        else:
            self.cart[product_id]["quantity"] += int(quantity)
        self.save()

    def remove(self, product: Product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids, is_active=True).select_related("category")
        products_map = {str(p.id): p for p in products}

        for product_id, item in self.cart.items():
            product = products_map.get(product_id)
            if not product:
                continue
            unit_price = Decimal(item["unit_price"])
            quantity = int(item["quantity"])
            yield {
                "product": product,
                "quantity": quantity,
                "unit_price": unit_price,
                "subtotal": unit_price * quantity,
            }

    def __len__(self):
        return sum(int(item["quantity"]) for item in self.cart.values())

    def get_total_price(self):
        total = Decimal("0.00")
        for item in self:
            total += item["subtotal"]
        return total
