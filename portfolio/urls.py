from django.urls import path
from . import views

urlpatterns = [
    path('', views.response_all_languages, name='all_languages_path'),
    path('<int:language_number>/', views.response_languages_by_number),
    path('<str:language>/', views.response_language, name='portfolio_path'),
]