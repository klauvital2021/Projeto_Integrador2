from django.contrib.auth.views import LogoutView
from django.urls import path

from backend.accounts import views as v

urlpatterns = [
    # path('login/', v.CustomLoginView.as_view(), name='login'),  # noqa E501
    path('login/', v.custom_login, name='login'),  # noqa E501
    path('logout/', LogoutView.as_view(), name='logout'),  # noqa E501
    path('responsavel/principal/add/', v.responsavel_principal_add, name='responsavel_principal_add'),   # noqa E501
]
