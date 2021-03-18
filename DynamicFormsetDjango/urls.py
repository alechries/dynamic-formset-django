from django.urls import path
from Example.views import example_view

urlpatterns = [
    path('', example_view),
]