import matplotlib.pyplot as plt
import numpy as np

y, x = np.meshgrid(np.linspace(-3, 3,100), np.linspace(-3, 3,100))

z = np.sin(x**2+y**2)
z = z[:-1, :-1]

ax = plt.subplot(111)

quad = plt.pcolormesh(x, y, z)

plt.colorbar()

plt.ion()
plt.show()

for phase in np.linspace(0,10*np.pi,200):
    z = np.sin(np.sqrt(x**2+y**2) + phase)
    z = z[:-1, :-1]

    quad.set_array(z.ravel())
    plt.title('Phase: %.2f'%phase)
    plt.draw()

plt.ioff()
plt.show()