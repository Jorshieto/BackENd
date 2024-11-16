from django.db import models

class Ticket(models.Model):

    #estos de aqui funcionan como desplegables 
    TIPOS_SERVICIO = [
        ('impresora', 'Impresion'),
        ('software', 'Software'),
        ('servidor', 'Servidor'),
        ('hardware', 'Hardware')
    ]
    
    PRIORIDADES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja')
    ]
    
    ENCARGADOS = [
        ('maniquil', 'Maria Aniquil'),
        ('gsoto', 'Guido Soto'),
        ('jmunoz', 'Jorge Munoz')
    ]

    AREAS = [
        ('recursos_humanos', 'Recursos Humanos'),
        ('finanzas', 'Finanzas'),
        ('marketing', 'Marketing '),
        ('ventas', 'Ventas'),
        ('atencion_al_cliente', 'Atencion al Cliente')
    ]
    #son los tipos de datos del formulario
    nombre = models.CharField(max_length=50)
    fono = models.CharField(max_length=9)
    email = models.EmailField()
    area = models.CharField(max_length=50, choices=AREAS)
    servicio = models.CharField(max_length=50, choices=TIPOS_SERVICIO)
    prioridad = models.CharField(max_length=50, choices=PRIORIDADES)
    encargado = models.CharField(max_length=50, choices=ENCARGADOS)
    descripcion_del_problema = models.TextField()
    def __str__(self):
        return self.nombre
