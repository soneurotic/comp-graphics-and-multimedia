import matplotlib.pyplot as plt 
import numpy as np

fig, ax = plt.subplots() #розбиття поля графіку на компоненти "figure" і "axes" 
fig.set_size_inches(10, 5.625) #задання розміру холста 960х540 пікселів (1 inch = 96px)

file = open("DS2.txt") #відкриття файлу з датасетом 
x = [] #масив що містить x-ові координати точок
y = [] #масив що містить у-ові координати точок

#розбиття рядків (пар координат) на компоненти х та у 
for row in file: 
    Coordinates = row.split(" ")
    x.append(Coordinates[0])
    y.append(Coordinates[1])

#переведення масивів у масиви пакету numpy
NumpyX = np.array(x, 'int16') 
NumpyY = np.array(y, 'int16')

#встановлення обмежень по осям х та у при відображенні графіку 
plt.xlim([int(min(x, key = lambda i: int(i))), int(max(x, key = lambda i: int(i)))])
plt.ylim([int(min(y, key = lambda i: int(i))), int(max(y, key = lambda i: int(i)))])

lines = plt.plot(NumpyX, NumpyY) #присвоєння відображення холсту змінній lines для редагування відображення ліній на наступному кроці
plt.setp(lines, linestyle = '') #видалення ліній, що з'єднують точки на холсті
ax.scatter(NumpyX, NumpyY, s=1) #задання найменшого розміру точок для зручності перегляду результату 
plt.grid() #створення сітки 
fig.savefig('Figure.png', dpi = 1000) #збереження графіку у формат png з роздільною здатністю 1000 dpi
plt.show() #відображення графіку