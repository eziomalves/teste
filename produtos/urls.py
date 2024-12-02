from .views import CreateCategoryView, ListCategoryView
from django.urls import path

urlpatterns = [
    path("category/add", CreateCategoryView.as_view(), name="create_category"),
    path("category", ListCategoryView.as_view(), name="list_category"),
]
