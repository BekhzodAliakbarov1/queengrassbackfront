from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('product-list/', views.ProductList, name="product-list"),
	path('product-list/<str:name>/', views.EachProductList),
	path('product-list/<str:name>/<str:pk>/', views.EachProductListItemDetail),
]