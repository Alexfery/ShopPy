from django.shortcuts import render
from catalog.models import Product

def home(request):
    best_sellers = Product.objects.filter(is_active=True).order_by("-created_at")[:6]
    return render(request, "core/home.html", {
        "best_sellers": best_sellers,
        "meta_title": "Tablouri din licheni — premium, eco, handmade",
        "meta_description": "Tablouri din licheni stabilizați (moss art). Design minimalist, personalizare, livrare rapidă.",
        "breadcrumbs": [{"label": "Acasă"}],
    })

def about(request):
    return render(request, "core/about.html", {
        "meta_title": "Despre — Tablouri din licheni",
        "meta_description": "Află povestea noastră și cum creăm tablouri din licheni stabilizați.",
        "breadcrumbs": [{"label": "Acasă", "url": "/"}, {"label": "Despre"}],
    })

def contact(request):
    return render(request, "core/contact.html", {
        "meta_title": "Contact — Tablouri din licheni",
        "meta_description": "Contactează-ne pentru ofertă, personalizări și întrebări.",
        "breadcrumbs": [{"label": "Acasă", "url": "/"}, {"label": "Contact"}],
    })
