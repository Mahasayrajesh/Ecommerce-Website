from django.urls import path
from accounts import views
urlpatterns = [
    path("",views.register,name="register"),
    path("index",views.index,name='index'),
    path("user_login",views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='logout'),
    path('details/<int:pk>/',views.details,name="details"),
    path("profile",views.profile,name='profile'),
    path("add_profile",views.add_profile,name="add_profile"),
    path('productliked/<int:pk>',views.product_liked,name="productliked"),
    path("wishlist",views.add_wishlist,name='wishlist'),
    path('search',views.searchproducts,name='search'),
    path("productcart/<int:pk>",views.add_to_cart,name='productcart'),
    path('cards',views.card,name="cards"),
    path('remove',views.remove_cart,name="remove"),
    path("succ",views.success,name="succ")


    
]
