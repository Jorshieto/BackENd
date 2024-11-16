function confirmAction(action, id) {  // Función para confirmar acciones (actualizar o eliminar)
    let message = '';  // Variable para almacenar el mensaje de confirmación
    if (action === 'actualizar') {
        message = `¿Estás seguro que quieres actualizar el ticket con ID ${id}?`;  // Mensaje de confirmación para actualización
        if (confirm(message)) {  // Si el usuario confirma
            window.location.href = `/actualizar_ticket/${id}`;  // Redirige a la URL de actualización
        }
    } else if (action === 'eliminar') {
        message = `¿Estás seguro que quieres eliminar el ticket con ID ${id}?`;  // Mensaje de confirmación para eliminación
        if (confirm(message)) {  // Si el usuario confirma
            window.location.href = `/eliminar_ticket/${id}`;  // Redirige a la URL de eliminación
        }
    }
}