from django.urls import path
from . import views

urlpatterns = [
    path('', views.author_list, name='author_list'),
    path('delete_author/<int:delete_id>/', views.delete_author, name='delete_author'),
    path('add_author/', views.add_author, name='add_author'),
    path('edit_author/<int:id>', views.edit_author, name='edit_author'),
]
