from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('assist/', views.assist, name='assist'),            # Home page → index.html
    path('ask-groq/', views.ask_groq, name='ask'),  # POST endpoint
]
