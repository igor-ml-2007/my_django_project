from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', category_page_view, name='category'),
    path('category_brand/<int:category_id>/', category_page_view_2, name='brand'),
    path('all_products/', all_products_page, name='all')
]