# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DBjHjqv2WoTe2uj9zwcq6lMEtSRwr-5L
"""

import matplotlib.pyplot as plt

import numpy as np

x=np.array([1,2,3,4,5,6,7

])

y=np.array([3,8,3,10,3,9,3])

plt.plot(x,y)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Yurak urishi uchun simulyatsiya qilingan ma'lumot
x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x) + 0.5 * np.sin(3 * x) + 0.2 * np.sin(10 * x) - 0.1 * np.exp(-(x - np.pi) ** 2 / 0.1)

# Grafikni chizish
plt.plot(x, y, color='red')
plt.title("Yurak urishi grafikasi")
plt.xlabel("Vaqt")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Uyning korpusi (to'rtburchak)
x_body = [2, 2, 8, 8, 2]
y_body = [0, 5, 5, 0, 0]

# Tom (uchburchak)
x_roof = [2, 5, 8, 2]
y_roof = [5, 8, 5, 5]

# Eshik (kichik to'rtburchak)
x_door = [4, 4, 6, 6, 4]
y_door = [0, 3, 3, 0, 0]

# Deraza (kichik to'rtburchak)
x_window = [3, 3, 4, 4, 3]
y_window = [4, 5, 5, 4, 4]

# Chizish
plt.plot(x_body, y_body, color='brown', label="Uy korpusi")
plt.plot(x_roof, y_roof, color='red', label="Tom")
plt.plot(x_door, y_door, color='blue', label="Eshik")
plt.plot(x_window, y_window, color='green', label="Deraza")

# Grafik sozlamalari
plt.axis('equal')
plt.title("Ikki qavatli uy shaklidagi grafik")
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x= np.array([0,1,2,3,4,5])
import matplotlib.pyplot as plt
import numpy as np

x= np.array([0,1,2,3,4,5])
y= np.array([0,2,8,1,14,7])
mycolor=['red','green','purple','lime','aqua','yellow']
size=[10,60,120,80,20,190]
plt.scatter(x,y,color=mycolor,s=size,
alpha=0.3)
plt.show()

plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([35,25,26,23,18])
mylabels=["kompyuter","elekronika","kiberhafsizli","malumotlar","suniy intellekt"]
plt.pie(x,labels=mylabels)
plt.show()

