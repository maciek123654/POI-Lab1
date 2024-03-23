import numpy as np
from scipy.stats import norm
from csv import writer


def gen_points_a(num_points: int = 2000):
    # norm - funkcja reprezentująca rozkład normlny
    # loc - średnia wartość oczekiwana dla rozkładu normalnego
    #       większość punktów ma być skupiona wokół wartości -10
    # scale - odchylenie standardowe dla rozkłdu normalnego
    #         większość punktów będzie skupiona wokół wartości średniej
    #         w zakresie około 20 jednostek
    dis_x = norm(loc=-10, scale=20)  # Szerokość 20
    dis_y = norm(loc=-10, scale=20)  # Długość 20
    dis_z = norm(loc=0, scale=0)

    # rvs generuje losowe próbki rozkłądu normalnego w zadanej ilości
    x = dis_x.rvs(size=num_points)
    y = dis_y.rvs(size=num_points)
    z = dis_z.rvs(size=num_points)
    points_a = zip(x, y, z)
    return points_a


def gen_points_b(num_points: int = 2000):
    dis_x = norm(loc=0, scale=10)
    dis_y = norm(loc=0, scale=0)
    dis_z = norm(loc=10, scale=5)

    x = dis_x.rvs(size=num_points)
    y = dis_y.rvs(size=num_points)
    z = dis_z.rvs(size=num_points)
    points_b = zip(x, y, z)
    return points_b


def gen_points_c(num_points: int = 2000):
    radius = 10
    theta = np.random.uniform(0, 2*np.pi, num_points)  # Generowanie losowych kątów wokół osi cylindra
    h = np.random.uniform(0, 60, num_points)  # Generowanie losowych wysokości w zakresie od 0 do 100

    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    points_c = [(x[i], y[i], h[i]) for i in range(num_points)]
    return points_c


cloud1 = gen_points_a(2000)
cloud2 = gen_points_b(2000)
cloud3 = gen_points_c(2000)
with open('LidarDataFlat.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
    csvwriter = writer(csvfile)
    for i in cloud1:
        csvwriter.writerow(i)
with open('LidarDataVertical.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
    csvwriter = writer(csvfile)
    for i in cloud2:
        csvwriter.writerow(i)
with open('LidatDataCilinder.xyz', 'w', encoding='utf-8', newline='\n') as csvfile:
    csvwriter = writer(csvfile)
    for i in cloud3:
        csvwriter.writerow(i)
