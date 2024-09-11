from products.models import Product
from django.contrib.auth.models import User

def get_cart_count(request):
    count = 0
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
            prods = Product.objects.filter(carts=user)
            count = prods.count()
        except Product.DoesNotExist:
            count = 0
    return {'count': count}
