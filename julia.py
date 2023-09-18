import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

xdlin, yvisot = 200, 200

t= complex(0.0,0.0)
zabs_max = 10
nit_max = 2000

xmin, xmax = -2, 2
xwidth = xmax - xmin
ymin, ymax = -2, 2
yheight = ymax - ymin

julia = np.zeros((xdlin, yvisot))


for ix in range(xdlin):
    for iy in range(yvisot):
        kol = 0
        z = complex(ix / xdlin * xwidth + xmin,
                    iy / yvisot * yheight + ymin)
        while abs(z) <= zabs_max and kol < nit_max:
            z = z**2 + t
            kol += 1
        ot= 1-np.sqrt(kol / nit_max)
        otno = kol / nit_max
        julia[ix,iy] = otno

fig, ax = plt.subplots()
ax.imshow(julia, interpolation='nearest', cmap=cm.hot)


plt.show()