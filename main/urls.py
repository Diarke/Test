from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test/<str:pk>', views.test_view, name='test-view')
]
