from AppSanta import views
from django.urls import path
from AppSanta import views_clases



urlpatterns = [
    path ('inicio/', views.inicio,name= 'inicio'),
    path ('productos/', views.productos, name= 'productos'),
    path ('proveedores/', views.proveedores, name= 'proveedores'),
    path ('clientes/', views.clientes, name= 'clientes'),
    path ('envios/', views.envios, name= 'envios'),
    path ('cliente-form/' , views.cliente_form, name= 'ClienteForm'),
    path ('producto-form-2/' , views.producto_form_2, name= 'ProductoForm2'),
    path ('productoFormulario/' , views.productoFormulario, name= 'productoFormulario'),
    path ('busquedaProducto/', views.busquedaProducto, name="BusquedaProducto"),
    path('buscar/', views.buscar),
    path('leerProducto/', views.leerProducto, name= 'leerProducto'),
    path('eliminarProducto/<producto_nombre>', views.eliminarProducto, name= 'EliminaProducto'),
]

urls_vista_clases= [
    path ('clases/lista/', views_clases.ClienteListView.as_view(),name= 'List'),
    path ('clases/detalle/<int:pk>/', views_clases.ClienteDetalle.as_view(), name= 'Details'),
    path ('clases/nuevo/', views_clases.ClienteCreateViews.as_view(), name= 'New'),
    path ('clases/editar/<int:pk>', views_clases.ClienteUdateView.as_view(), name= 'Edit'),
    path ('clases/eliminar/<int:pk>', views_clases.ClienteDeleteView.as_view(), name= 'Delete'),
]
urlpatterns += urls_vista_clases