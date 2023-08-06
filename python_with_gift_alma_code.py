
import random

name = ["Ali", "Ayşe", "Mehmet", "Kenan", "İrem", "Tuğba"]

def draw():
    area = name.copy()
    giving = name.copy()

    # area = alan ve giving = veren .

    while len(area) > 0:
        area_index = random.randint(0, len(area) - 1)
        giving_index = random.randint(0, len(giving) - 1)


        while area[area_index] == giving[giving_index]:
            area_index = random.randint(0, len(area) - 1)
            giving_index = random.randint(0, len(giving) - 1)

        print(area[area_index], "hediye alıyor", giving[giving_index])

        area.remove(area[area_index])
        giving.remove(giving[giving_index])

draw()
