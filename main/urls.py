from django.urls import path
from . import views

urlpatterns = [
    path('', views.main , name='main'),
    path('about/', views.about , name='about'),
    path('contact/', views.contact , name='contact'),
    path('work/', views.work , name='work'),
    path('work/category/<int:category_id>/', views.tapes, name='tapes'),
]