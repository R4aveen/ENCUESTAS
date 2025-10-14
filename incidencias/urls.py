from django.urls import path
from . import views
from . import views_clasificacion

app_name = "incidencias"

urlpatterns = [
    # URLs de Categorías
    path("categorias/", views_clasificacion.categoria_lista, name="categoria_lista"),
    path("categorias/nueva/", views_clasificacion.categoria_crear, name="categoria_crear"),
    path("categorias/<int:pk>/editar/", views_clasificacion.categoria_editar, name="categoria_editar"),
    path("categorias/<int:pk>/toggle/", views_clasificacion.categoria_toggle, name="categoria_toggle"),
    path("categorias/<int:pk>/eliminar/", views_clasificacion.categoria_eliminar, name="categoria_eliminar"),
    
    # API endpoints
    path("api/cuadrillas-por-departamento/<int:departamento_id>/", views.cuadrillas_por_departamento, name="cuadrillas_por_departamento"),

    # URLs de Tipos de Incidencia
    path("tipos/", views_clasificacion.tipo_lista, name="tipo_lista"),
    path("tipos/nuevo/", views_clasificacion.tipo_crear, name="tipo_crear"),
    path("tipos/<int:pk>/editar/", views_clasificacion.tipo_editar, name="tipo_editar"),
    path("tipos/<int:pk>/toggle/", views_clasificacion.tipo_toggle, name="tipo_toggle"),
    path("tipos/<int:pk>/eliminar/", views_clasificacion.tipo_eliminar, name="tipo_eliminar"),

    path("incidencias/", views.incidencias_lista, name ="incidencias_lista"),
    path("incidencias/nuevo/", views.incidencia_crear, name = "incidencia_crear"),
    path("incidencias/<int:pk>/", views.incidencia_editar, name = "incidencia_editar") ,
    path("incidencias/<int:pk>/detalle/", views.incidencia_detalle, name = "incidencia_detalle"), 
    path("incidencias/<int:pk>/eliminar/", views.incidencia_eliminar, name = "incidencia_eliminar"), 
]