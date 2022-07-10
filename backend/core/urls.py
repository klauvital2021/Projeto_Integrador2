from django.urls import path

from backend.core import views as v

urlpatterns = [
    path('', v.home, name='home')
]
