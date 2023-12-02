from django.shortcuts import render
from .models import FAQ

# Create your views here.


def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, "faqs/faq_list.html", {"faqs": faqs})
