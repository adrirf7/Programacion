tareas = [
    {"tarea": "Reunión con el cliente para revisión de requerimientos", "urgente": True},
    {"tarea": "Preparar informe semanal de progreso", "urgente": False},
    {"tarea": "Entrega del prototipo funcional al cliente", "urgente": True},
    {"tarea": "Coordinación con el equipo de diseño", "urgente": False},
    {"tarea": "Revisión del presupuesto del proyecto", "urgente": False},
    {"tarea": "Resolución de problemas técnicos con el equipo de desarrollo", "urgente": True},
    {"tarea": "Presentación del plan de proyecto al comité ejecutivo", "urgente": True},
    {"tarea": "Capacitación al equipo en nuevas herramientas", "urgente": False},
    {"tarea": "Revisión final del contrato con proveedores", "urgente": True},
    {"tarea": "Actualización del cronograma de entregas", "urgente": False}
]

def tareasUrgentes(tarea):
    return tarea["urgente"]== True

resultado= filter(tareasUrgentes, tareas)

for i in resultado:
    print(i["tarea"])