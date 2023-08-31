from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('buy/<int:pk>/',views.buy,name='buy'),
    path('pdf/',views.pdf,name='pdf'),
    path('adding_product', views.product_create, name='product_create')
]