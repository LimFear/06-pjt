from django.urls import path, include
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),

    # Thread
    path('<int:book_pk>/threads/create/', views.thread_create, name='thread_create'),
    path('threads/<int:pk>/', views.thread_detail, name='thread_detail'),
    path('threads/<int:pk>/update/', views.thread_update, name='thread_update'),
    path('threads/<int:pk>/delete/', views.thread_delete, name='thread_delete'),
]
