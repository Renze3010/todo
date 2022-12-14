from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_view, name="create"),
    path('delete/<int:pk>/', views.delete_view, name='delete')
]
