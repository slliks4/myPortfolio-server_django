# Imports
from django.urls import path
from .views import IndexPage

# URL PATTERNS
urlpatterns = [
    path('', IndexPage, name="index"),
]
