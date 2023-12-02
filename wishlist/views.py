from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404,
    HttpResponseRedirect,
)
from django.contrib import messages
from django.http import Http404

from .models import Wishlist
from profiles.models import UserProfile
from products.models import Product

# Create your views here.


def view_wishlist(request):
    """
    Show a user's wishlist
    """

    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry, you need to be logged in to add to your Wishlist."
        )
        return redirect(reverse("account_login"))

    user = get_object_or_404(UserProfile, user=request.user)
    # https://www.queworx.com/django/django-get_or_create/
    wishlist, created = Wishlist.objects.get_or_create(user=user.user)

    template_name = "wishlist/wishlist.html"
    context = {"wishlist": wishlist}
    return render(request, template_name, context)
