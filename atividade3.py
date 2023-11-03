class Monitor:
    def _init_(self, modelo):
        self.modelo = modelo

class Computador:
    def _init_(self, marca):
        self.marca = marca
        self.monitor = None

    def conectar_monitor(self, monitor):
        self.monitor = monitor

monitor1 = Monitor("Monitor A")
monitor2 = Monitor("Monitor B")

computador1 = Computador("Computador 1")
computador2 = Computador("Computador 2")

computador1.conectar_monitor(monitor1)

print(f"O {computador1.marca} está conectado ao {computador1.monitor.modelo}.")

print(f"O {computador2.marca} não está conectado a um monitor.")