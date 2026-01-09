from django.urls import path
from .views import home
# from .views import success

urlpatterns = [
    path('', home, name='home'),
]
