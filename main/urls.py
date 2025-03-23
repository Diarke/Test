from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='home'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),
    path('news/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete'),
    path('news/create/', views.news_form, name='news_form'),
    path('tests/', views.index, name='tests'),
    path('test/<int:pk>/', views.test_view, name='test-view'),
    path('history/', views.history, name='history'),
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('otzivi/', views.otzv, name='otzv'),
]
