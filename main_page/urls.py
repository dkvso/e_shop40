from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('<int:pk', views.get_full_product),
    path('<int:pk', views.get_full_product)
]