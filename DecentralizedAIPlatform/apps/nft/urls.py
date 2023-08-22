
from django.urls import path
from . import views

app_name = 'nft'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:nft_id>/', views.detail, name='detail'),
]
