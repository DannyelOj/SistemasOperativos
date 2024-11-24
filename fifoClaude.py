from random import randint


class ProcesoFIFO:
    def __init__(self):
        self.procesos = []
        self.tiempo_actual = 0

    def agregar_proceso(self, nombre, tiempo_llegada, tiempo_ejecucion):
        self.procesos.append({
            'nombre': nombre,
            'llegada': tiempo_llegada,
            'ejecucion': tiempo_ejecucion,
            'inicio': None,
            'fin': None,
            'espera': None
        })

    def ejecutar_simulacion(self):
        # Ordenamos los procesos por tiempo de llegada
        self.procesos.sort(key=lambda x: x['llegada'])

        # Para cada proceso, calculamos sus tiempos
        tiempo_actual = 0

        print("\n=== SIMULACIÓN DE PROCESOS FIFO ===")
        print("\nProceso | Llegada | Ejecución | Inicio | Fin | Tiempo Espera")
        print("-" * 60)

        for proceso in self.procesos:
            # El proceso no puede iniciar antes de su tiempo de llegada
            if tiempo_actual < proceso['llegada']:
                tiempo_actual = proceso['llegada']

            proceso['inicio'] = tiempo_actual
            proceso['fin'] = tiempo_actual + proceso['ejecucion']
            proceso['espera'] = proceso['inicio'] - proceso['llegada']

            # Actualizamos el tiempo actual
            tiempo_actual = proceso['fin']

            print(
                f"{proceso['nombre']:7} | {proceso['llegada']:7} | {proceso['ejecucion']:9} | {proceso['inicio']:6} | {proceso['fin']:3} | {proceso['espera']:12}")

    def mostrar_estadisticas(self):
        tiempo_espera_total = sum(p['espera'] for p in self.procesos)
        tiempo_espera_promedio = tiempo_espera_total / len(self.procesos)
        tiempo_total_ejecucion = max(p['fin'] for p in self.procesos)

        print("\n=== ESTADÍSTICAS ===")
        print(f"Tiempo promedio de espera: {tiempo_espera_promedio:.2f} unidades de tiempo")
        print(f"Tiempo total de ejecución: {tiempo_total_ejecucion} unidades de tiempo")

        # Mostramos el diagrama de Gantt
        print("\n=== DIAGRAMA DE GANTT ===")
        for proceso in self.procesos:
            print(f"\nProceso {proceso['nombre']}: ", end="")
            # Espacios hasta el inicio
            print("." * proceso['llegada'], end="")
            # Espera
            print("-" * int(proceso['espera']), end="")
            # Ejecución
            print("#" * proceso['ejecucion'], end="")
        print("\n")
        print("Leyenda:")
        print(". = Aún no llega")
        print("- = Esperando")
        print("# = Ejecutando")


# Crear instancia de la simulación
simulacion = ProcesoFIFO()

# Agregar los 4 procesos con tiempos aleatorios
procesos = [
    ('A', randint(0, 5), randint(2, 6)),  # (nombre, tiempo_llegada, tiempo_ejecucion)
    ('B', randint(1, 6), randint(2, 6)),
    ('C', randint(2, 7), randint(2, 6)),
    ('D', randint(3, 8), randint(2, 6))
]

for nombre, llegada, ejecucion in procesos:
    simulacion.agregar_proceso(nombre, llegada, ejecucion)

# Ejecutar la simulación
simulacion.ejecutar_simulacion()
simulacion.mostrar_estadisticas()