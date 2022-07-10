from django.urls import include, path

from backend.crm import views as v

dependente_urlpatterns = [
    path('', v.DependenteListView.as_view(), name='dependente_list'),  # noqa E501
    path('<int:pk>/', v.DependenteDetailView.as_view(), name='dependente_detail'),  # noqa E501
    path('add/', v.DependenteCreateView.as_view(), name='dependente_add'),  # noqa E501
    path('edit/<int:pk>/', v.DependenteUpdateView.as_view(), name='dependente_edit'),  # noqa E501
    path('delete/<int:pk>/', v.dependente_delete, name='dependente_delete'),  # noqa E501

]

familia_urlpatterns = [
    path('', v.FamiliaListView.as_view(), name='familia_list'),  # noqa E501
    path('<int:pk>/', v.FamiliaDetailView.as_view(), name='familia_detail'),  # noqa E501
    path('add/', v.FamiliaCreateView.as_view(), name='familia_add'),  # noqa E501
    path('edit/<int:pk>/', v.FamiliaUpdateView.as_view(), name='familia_edit'),  # noqa E501
    path('delete/<int:pk>/', v.familia_delete, name='familia_delete'),  # noqa E501

]

responsavel_urlpatterns = [
    path('', v.ResponsavelListView.as_view(), name='responsavel_list'),  # noqa E501
    path('<int:pk>/', v.ResponsavelDetailView.as_view(), name='responsavel_detail'),  # noqa E501
    path('add/', v.ResponsavelCreateView.as_view(), name='responsavel_add'),  # noqa E501
    path('edit/<int:pk>/', v.ResponsavelUpdateView.as_view(), name='responsavel_edit'),  # noqa E501
    path('delete/<int:pk>/', v.responsavel_delete, name='responsavel_delete'),  # noqa E501

]

cuidador_urlpatterns = [
    path('', v.CuidadorListView.as_view(), name='cuidador_list'),  # noqa E501
    path('<int:pk>/', v.CuidadorDetailView.as_view(), name='cuidador_detail'),  # noqa E501
    path('add/', v.CuidadorCreateView.as_view(), name='cuidador_add'),  # noqa E501
    path('edit/<int:pk>/', v.CuidadorUpdateView.as_view(), name='cuidador_edit'),  # noqa E501
    path('delete/<int:pk>/', v.cuidador_delete, name='cuidador_delete'),  # noqa E501

]

urlpatterns = [
    path('dependente/', include(dependente_urlpatterns)),
    path('familia/', include(familia_urlpatterns)),
    path('responsavel/', include(responsavel_urlpatterns)),
    path('cuidador/', include(cuidador_urlpatterns)),
]
