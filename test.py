import numpy as np
from basicplot import plot
import matplotlib.pyplot as pt
a = np.arange(1,10,0.2)
b = a**2

# fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10,5))
# plot(a,b,size=(8,8), xtitle='X-axis', ytitle='Y-axis', fontsize=25, xticks=range(1,11,2),ticklength=8)
# plot(a,b, ax=ax2,size=(8,8), xtitle='X-axis', fontsize=25, xticks=range(1,11,2),ticklength=8)
a = plot(a,b, xtitle='X-axis', ytitle='Y-axis', fontsize=20, size=(8,8), xticks=range(0,11), tickwidth=1.8, yticks=range(0,101,10))
# a.save('test.png')
# print(a.x)
# import sys
# print(pt not in sys.modules)