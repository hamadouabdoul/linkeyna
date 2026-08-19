from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('conversion/', views.conversion_page, name="conversion_page"),
    path('resultat/<str:id>/', views.resultat, name="resultat_page"),
    path('redirect/<str:new_link>', views.redirection, name="rediretion")
]