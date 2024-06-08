"""
    Programa que utiliza da biblioteca 'threading' para que dois processos rodem
    simultaneamente ao invés de esperar por outro terminar.
"""
from threading import Thread
import time


def car(speed, pilot):
    route = 0
    while route <= 100:
        print(f"Pilot: {pilot}, Km: {route}")
        route += speed
        time.sleep(0.5)


t_car1 = Thread(target=car, args=[1, 'Guilherme'])
t_car2 = Thread(target=car, args=[2, 'Python'])

t_car1.start()
t_car2.start()
