import pygame
import requests
import sys
import os
import OpenSkyAPICaller
from map import get_map

print("The OpenSky Network, http://www.opensky-network.org or by citing the paper Bringing up OpenSky: A large-scale ADS-B sensor network for research Matthias Schäfer, Martin Strohmeier, Vincent Lenders, Ivan Martinovic, Matthias WilhelmACM/IEEE International Conference on Information Processing in Sensor Networks, April 2014")
response = None
MYEVENTTYPE = 30
# Частота обновлениея ~20 секунд
# Сделано для того чтобы не нагружать систему

slovar = OpenSkyAPICaller.fetch()
slovar1, slovar = slovar[0], slovar[1][:-1]

try:
    x = [30, 50, 8, "map.png"]  # input().split()
    print(OpenSkyAPICaller.fetch()[1])
    map_file = get_map(x[0], x[1], x[2], x[3],
                       OpenSkyAPICaller.fetch()[1][:-1])
except IOError as ex:
    print("Ошибка записи временного файла:", ex)
    sys.exit(2)

# Инициализируем pygame
pygame.init()
pygame.time.set_timer(MYEVENTTYPE, 100000)
screen = pygame.display.set_mode((500, 400))
# Рисуем картинку, загружаемую из только что созданного файла.

screen.blit(pygame.image.load(x[3]), (0, 0))
# Переключаем экран и ждем закрытия окна.

pygame.display.flip()
running = True
x[2] = int(x[2])
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Обновление положения самолетов
        if event.type == MYEVENTTYPE:
            print("Мое событие сработало")
            slovar = OpenSkyAPICaller.fetch()
            slovar1, slovar = slovar[0], slovar[1][:-1]
            map_file = get_map(x[0], x[1], x[2], x[3], slovar)

        if event.type == pygame.KEYUP:
            # Сделано для проверки координат
            # Масштаб
            if event.key == pygame.K_PLUS:
                if x[2] != 20:
                    x[2] += 1

            if event.key == pygame.K_MINUS:
                if x[2] != 0:
                    x[2] -= 1
            # Перемещение камеры
            if event.key == pygame.K_UP:
                if x[1] != 73:
                    x[1] += 1

            if event.key == pygame.K_DOWN:
                if x[1] != 0:
                    x[1] -= 1

            if event.key == pygame.K_RIGHT:
                if x[0] != 180:
                    x[0] += 1

            if event.key == pygame.K_LEFT:
                if x[0] != -140:
                    x[0] -= 1
            if event.key == 105:
                xstat = input("Какой самолет вам нужен?")
                if xstat.isdigit():
                    print("Готово")
                    print("ICAO24:", str(slovar1[int(xstat)][0]), "Callsign:", str(slovar1[int(xstat)][1]), "Speed:", str(
                        slovar1[int(xstat)][5]) + "m/s", "On Ground?", str("No" if slovar1[int(xstat)][8] == False else "Yes"))
            map_file = get_map(x[0], x[1], x[2], x[3], slovar)

    # Создаем новую карту
    x[2] = abs(x[2])
    screen.blit(pygame.image.load(x[3]), (0, 0))
    pygame.display.flip()
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(x[3])
