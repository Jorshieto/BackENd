
from django.contrib import admin
from django.urls import path
from firstApp import views as firstApp_views  # Importar vistas de firstApp
from loginApp import views as loginApp_views    # Importar vistas de loginApp
#tuve que agregar alias por que sino se taldeaba 

urlpatterns = [
    #estas son las url de first app
    path('admin/', admin.site.urls),
    path('', firstApp_views.PaginaInicio, name='PaginaInicio'),
    path('crear_ticket/', firstApp_views.crear_ticket, name='crear_ticket'),
    path('crud/', firstApp_views.crud, name='crud'),
    path('crud_jefe_area/', firstApp_views.crud_jefe_area, name='crud_jefe_area'),  # Vista para jefe_area
    path('crud_soporte/', firstApp_views.crud_soporte, name='crud_soporte'),  # Vista para soporte
    path('actualizar_ticket/<int:id>/', firstApp_views.actualizar_ticket, name='actualizar_ticket'),# <int:id> sirve para actualizar un ticket específico mediante su ID
    path('actualizar_ticket_soporte/<int:id>/', firstApp_views.actualizar_ticket_soporte, name='actualizar_ticket_soporte'),
    path('eliminar_ticket/<int:id>/', firstApp_views.eliminar_ticket, name='eliminar_ticket'),
    
   # URLs de login app
    path('login/', loginApp_views.login_usuario, name='login'),  # Asegúrate de usar `login_usuario`
    path('registro/', loginApp_views.registro, name='registro'),
    path('logout/', loginApp_views.cerrar_sesion, name='logout'),
]

