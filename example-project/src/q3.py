import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x ve y değerlerini oluştur
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)

# x ve y değerlerinden ızgara (grid) oluştur
X, Y = np.meshgrid(x, y)

# Düzlem denklemi: z = 4 - x - y
Z = 4 - X - Y

# Grafiği oluştur
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Düzlemi çiz
ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100, color='r', edgecolors='w')

# Eksen etiketleri
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Başlık
ax.set_title('3D Plane of Equation x + y + z - 4 = 0')

# Göster
plt.show()
