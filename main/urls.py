from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test/<int:pk>', views.test_view, name='test-view')
]
