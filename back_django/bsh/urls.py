from django.urls import path

from bsh import views

urlpatterns = [
#   Decorator based vs class based
#   path('', views.bsh_list),
    path('', views.BshList.as_view()),
#   path('<int:pk>/', views.bsh_detail),
    path('<int:pk>/', views.BshDetail.as_view(),)
]