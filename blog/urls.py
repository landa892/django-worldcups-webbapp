from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('worldcups/', views.WorldCupListView.as_view(), name='worldcup_list'),
    path('worldcups/new/', views.WorldCupCreateView.as_view(), name='worldcup_create'),
    path('worldcups/<int:pk>/', views.WorldCupDetailView.as_view(), name='worldcup_detail'),
    path('worldcups/<int:pk>/edit/', views.WorldCupUpdateView.as_view(), name='worldcup_update'),
    path('worldcups/<int:pk>/delete/', views.WorldCupDeleteView.as_view(), name='worldcup_delete'),
    path('search/', views.search_worldcup, name='search'),
]
