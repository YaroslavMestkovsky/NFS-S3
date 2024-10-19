from django.urls import path
from . import views

urlpatterns = [
    path('doclist', views.document_list, name='document_list'),
    path('upload/', views.upload_document, name='upload_document'),
    path('delete/<int:pk>/', views.delete_document, name='delete_document'),
    path('welcome/', views.welcome, name='welcome'),
]
