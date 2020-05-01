from django.urls import path

from post import views

urlpatterns = [
  path('', views.post_list),
  path('<int:pk>/', views.post_detail),
]