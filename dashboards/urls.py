from django.urls import path
from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_category, name='add_category'),
    path('categories/edit/<int:pk>/', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>/', views.delete_category, name='delete_category'),

    path('post/', views.post, name='post' ),
    path('post/add/', views.add_post, name='add_post'),
    path('post/edit/<int:pk>/', views.edit_post, name='edit_post'),
    path('post/delete/<int:pk>/', views.delete_post, name='delete_post'),

    path('users/', views.users, name="users"),
    path('users/add/', views.add_users, name="add_users"),
    path('users/edit/<int:pk>/', views.edit_users, name="edit_users"),
    path('users/delete/<int:pk>/', views.delete_users, name="delete_users"),

]