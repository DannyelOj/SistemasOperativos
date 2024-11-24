from collections import deque


# Definimos una clase para los procesos
class Process:
    def __init__(self, pid, arrival_time, burst_time):
        """
        Inicializa un proceso.
        - pid: Identificador único del proceso.
        - arrival_time: Tiempo en que el proceso llega al sistema.
        - burst_time: Tiempo requerido para ejecutarse (duración).
        """
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time


# Función para ejecutar el algoritmo FIFO
def fifo_scheduling(processes):
    """
    Simula la planificación de procesos usando el algoritmo FIFO.
    - processes: Lista de procesos que llegan al sistema.
    """
    # Ordenamos los procesos por tiempo de llegada
    processes.sort(key=lambda x: x.arrival_time)

    # Inicializamos las variables necesarias
    queue = deque(processes)  # Usamos una cola para mantener el orden FIFO
    current_time = 0  # Tiempo actual del sistema
    schedule = []  # Lista para almacenar el orden de ejecución
    waiting_time = 0  # Tiempo de espera acumulado

    print("Simulación de FIFO")
    print("-" * 40)

    # Procesamos la cola
    while queue:
        process = queue.popleft()  # Obtenemos el primer proceso de la cola
        if current_time < process.arrival_time:
            # Si el proceso llega después del tiempo actual, adelantamos el reloj
            current_time = process.arrival_time

        # Registramos el inicio de la ejecución
        print(f"Tiempo {current_time}: Ejecutando proceso {process.pid}")

        # Calculamos el tiempo de espera para este proceso
        waiting_time += current_time - process.arrival_time

        # Añadimos el proceso al cronograma
        schedule.append((process.pid, current_time, current_time + process.burst_time))

        # Actualizamos el tiempo actual según el burst_time
        current_time += process.burst_time

    # Calculamos el tiempo promedio de espera
    avg_waiting_time = waiting_time / len(processes)

    print("\nResumen de Ejecución")
    print("-" * 40)
    for pid, start, end in schedule:
        print(f"Proceso {pid}: Inicio = {start}, Tiempo de Ejecucion = {end + 1}, Fin = {end}")

    print(f"\nTiempo promedio de espera: {avg_waiting_time:.2f}")


# Crear procesos de ejemplo
processes = [
    Process(pid=1, arrival_time=0, burst_time=4),
    Process(pid=2, arrival_time=2, burst_time=3),
    Process(pid=3, arrival_time=4, burst_time=1),
    Process(pid=4, arrival_time=6, burst_time=5)
]

# Ejecutar la simulación FIFO
fifo_scheduling(processes)
