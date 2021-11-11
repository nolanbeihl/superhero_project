from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('update/<int:hero_id>/', views.update, name='update'),
    path('delete/<int:hero_id>/', views.delete, name='delete'),
    path('index/', views.index, name='return'),
]

