from django.urls import path
from example import views

urlpatterns = [
    path('', views.example_view, name='example'),
    path('add-type-a', views.add_addition_type_a_view, name='add-type-a')
]