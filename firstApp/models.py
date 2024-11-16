from django.db import models

class Ticket(models.Model):

    # Estos son los valores para los desplegables
    TIPOS_SERVICIO = [
        ('impresora', 'Impresión'),
        ('software', 'Software'),
        ('servidor', 'Servidor'),
        ('hardware', 'Hardware'),
    ]
    
    PRIORIDADES = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]
    
    ENCARGADOS = [
        ('maniquil', 'Maria Aniquil'),
        ('gsoto', 'Guido Soto'),
        ('jmunoz', 'Jorge Munoz'),
    ]

    AREAS = [
        ('finanzas', 'Finanzas'),
        ('marketing', 'Marketing'),
        ('ventas', 'Ventas'),
    ]

    ESTADOS = [
        ('abierto', 'Abierto'),
        ('cerrado', 'Cerrado'),
        ('en_proceso', 'En Proceso'),
    ]    

    SATISFACCION = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja'),
    ]
    
    # Campos del modelo
    nombre = models.CharField(max_length=50)
    fono = models.CharField(max_length=9)
    email = models.EmailField()
    area = models.CharField(max_length=50, choices=AREAS)
    servicio = models.CharField(max_length=50, choices=TIPOS_SERVICIO)
    prioridad = models.CharField(max_length=50, choices=PRIORIDADES)
    encargado = models.CharField(max_length=50, choices=ENCARGADOS)
    descripcion = models.TextField(null=True, blank=True)  # Campo opcional

    # Estado: Definir valor por defecto 'abierto', que es un valor válido en ESTADOS
    estado = models.CharField(max_length=50, choices=ESTADOS)  # El valor por defecto debe ser uno de los valores en ESTADOS
    retroalimentacion_soporte = models.TextField(null=True, blank=True)  # Campo opcional
    satisfaccion_cliente = models.CharField(max_length=50, choices=SATISFACCION)

    def __str__(self):
        return self.nombre
