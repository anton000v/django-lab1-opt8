from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPage.as_view()),
    path('check-answer/', views.CheckAnswer.as_view()),
    path('admin-page/', views.AdminPage.as_view(), name='admin-page'),
]