from django.urls import path
from . import views

urlpatterns = [
    path('', views.MessageListView.as_view(), name='message_list'),
    path('new/', views.MessageCreateView.as_view(), name='message_create'),
    path('<int:pk>/', views.MessageDetailView.as_view(), name='message_detail'),
]
