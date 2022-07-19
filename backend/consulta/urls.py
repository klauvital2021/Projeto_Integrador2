from django.urls import include, path

from backend.consulta import views as v

consulta_urlpatterns = [
    path('', v.ConsultaListView.as_view(), name='consulta_list'),  # noqa E501
    path('<int:pk>/', v.ConsultaDetailView.as_view(), name='consulta_detail'),  # noqa E501
    path('add/', v.ConsultaCreateView.as_view(), name='consulta_add'),  # noqa E501
    path('edit/<int:pk>/', v.ConsultaUpdateView.as_view(), name='consulta_edit'),  # noqa E501
    path('delete/<int:pk>/', v.consulta_delete, name='consulta_delete'),  # noqa E501
]

posconsulta_urlpatterns = [
    path('', v.PosConsultaListView.as_view(), name='posconsulta_list'),  # noqa E501
    path('<int:pk>/', v.PosConsultaDetailView.as_view(), name='posconsulta_detail'),  # noqa E501
    path('add/<int:consulta_pk>/', v.PosConsultaCreateView.as_view(), name='posconsulta_add'),  # noqa E501
    path('edit/<int:pk>/', v.PosConsultaUpdateView.as_view(), name='posconsulta_edit'),  # noqa E501
    path('delete/<int:pk>/', v.posconsulta_delete, name='posconsulta_delete'),  # noqa E501
]

medicamento_urlpatterns = [
    path('', v.MedicamentoListView.as_view(), name='medicamento_list'),  # noqa E501
    path('<int:pk>/', v.MedicamentoDetailView.as_view(), name='medicamento_detail'),  # noqa E501
    path('add/', v.MedicamentoCreateView.as_view(), name='medicamento_add'),  # noqa E501
    path('edit/<int:pk>/', v.MedicamentoUpdateView.as_view(), name='medicamento_edit'),  # noqa E501
    path('delete/<int:pk>/', v.medicamento_delete, name='medicamento_delete'),  # noqa E501
]


urlpatterns = [
    path('consulta/', include(consulta_urlpatterns)),
    path('posconsulta/', include(posconsulta_urlpatterns)),
    path('medicamento/', include(medicamento_urlpatterns)),
]
