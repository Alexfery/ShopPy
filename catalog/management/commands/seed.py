from django.core.management.base import BaseCommand
from django.utils.text import slugify
from decimal import Decimal
from catalog.models import Category, Product

class Command(BaseCommand):
    help = "Seed demo data (categories + 8 products)"

    def handle(self, *args, **options):
        categories = [
            "Minimal",
            "Premium",
            "Personalizate",
        ]

        cat_objs = {}
        for name in categories:
            c, _ = Category.objects.get_or_create(
                slug=slugify(name),
                defaults={"name": name},
            )
            cat_objs[name] = c

        products = [
            ("Tablou Lichen Nordik", "Minimal", "Design nordic, textură fină, ramă discretă.", "399.00", 10),
            ("Moss Frame Minimal", "Minimal", "Cadru minimalist cu licheni stabilizați.", "349.00", 8),
            ("Emerald Premium Panel", "Premium", "Compoziție premium cu volum și contrast.", "699.00", 5),
            ("Forest Depth Premium", "Premium", "Look premium, ideal pentru spații moderne.", "749.00", 3),
            ("Personalizat Logo Office", "Personalizate", "Tablou personalizat cu logo (ideal birouri).", "999.00", 2),
            ("Monogram Moss Signature", "Personalizate", "Inițiale/monogram, stil premium.", "899.00", 2),
            ("Cloud Dancer Series", "Minimal", "Seria Cloud Dancer — lumină, aerisire, calm.", "429.00", 6),
            ("Electric Accent Moss", "Premium", "Accente vizuale puternice, vibe modern.", "799.00", 4),
        ]

        created = 0
        for name, cat_name, desc, price, stock in products:
            slug = slugify(name)
            _, was_created = Product.objects.get_or_create(
                slug=slug,
                defaults={
                    "name": name,
                    "category": cat_objs[cat_name],
                    "description": desc,
                    "price": Decimal(price),
                    "currency": "RON",
                    "stock": stock,
                    "is_active": True,
                },
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Seed done. New products: {created}"))
