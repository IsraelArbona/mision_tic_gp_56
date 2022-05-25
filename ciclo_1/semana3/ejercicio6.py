# Realización de un CRUD

tareas = {
    '01': {
        'descripcion':'Ir a mercar',
        'estado': 'pendiente',
        'tiempo': 60
    },
    '02': {
        'descripcion': 'estudiar',
        'estado': 'pendiente',
        'tiempo': 180
    },
    '03': {
        'descripcion': 'Hacer ejercicio',
        'estado': 'pendiente',
        'tiempo': 50

    }
}

# Crear una nueva tarea.
def create(tareas,identificador,tareasNueva):
    tareas[identificador] = tareasNueva
    return tareas

# Listar la tareas
def read(tareas):
    for identificador,tarea in tareas.items():
        print(identificador, ' - ', end = '')
        for clave, valor in tarea.items():
            print(valor, ', ', end='')
        print()
    print()

def validarTarea(identificador,tareas):
    if identificador in tareas:
        return True
    else:
        False

opcion = 0
while opcion != 5:

    print('\n --- Aplicación del CRUD tareas pendientes --- \n')
    print(' 1: Adicionar Tarea ')
    print(' 2: Consultar Tarea ')
    print(' 3: Actualizar Tarea ')
    print(' 4: Eliminar Tarea ')
    print(' 5: Salir \n')

    opcion = int(input('Ingrese la opcion : '))

    if opcion == 1:
        print('\n-> Adicionar la tarea \n')

        identificador = str(input('Ingresar el identificador de la tarea: '))

        if validarTarea(identificador, tareas) == False:
            descripcion = str(input('Ingresar la descripción de la tarea: '))
            estado = str(input('Ingresar el estado de la tarea: '))
            tiempo = int(input('Ingresar el tiempo de la tarea: '))

            tareasNueva = {
                'descripcion': descripcion,
                'estado': estado,
                'tiempo': tiempo
            }

            # función para agregar una tarea
            tareas = create(tareas,identificador,tareasNueva)

    elif opcion == 2:
        print()
        print('-> Listado de tareas')
        print()

        # función para listar las tareas
        read(tareas)
    elif opcion == 3:
        print()
        print('-> Actulizar Tarea')
        print()

        identificador = str(input('Ingrese el identificador de la tarea para modificar : '))

        if validarTarea(identificador,tareas):
            nuevaDescripcion = str(input('Nueva descripción : '))
            if nuevaDescripcion:
                tareas[identificador]['descripcion'] = nuevaDescripcion
            nuevoEstado = str(input('Nuevo estado : '))
            if nuevoEstado:
                tareas[identificador]['estado'] = nuevoEstado
            nuevoTiempo = int(input('Nuevo tiempo : '))
            if nuevoTiempo:
                tareas[identificador]['tiempo'] = nuevoTiempo
        else:
            print('No ha sido encontrada la tarea.')
    elif opcion == 4:
        print()
        print('-> Eliminar Tarea')
        print()

        identificador = str(input('Ingrese el identificador de la tarea a eliminar : '))

        if validarTarea(identificador, tareas):
            tareas.pop(identificador)
        else:
            print('La tarea pendiente no fue eliminada.')
