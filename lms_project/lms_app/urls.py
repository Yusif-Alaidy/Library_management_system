from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('books/',views.Books, name='books'),
    path('update/<int:id>',views.Update, name='update'),
    path('delete/<int:id>',views.Delete, name='delete'),
]