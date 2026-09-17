import numpy as np
import matplotlib.pyplot as plt
import SimpleITK as sitk
from pathlib import Path

#%%

tpts = ['P0', 'P2', 'P4', 'P8', 'P16', 'P32', 'Adult']

view = 'sag'
vmax = 1200

range_axi = [[0,240],[90,330]]
range_cor = [[0,145],[0,330]]
range_sag = [[0,140],[90,340]]
sl_axi = 82
sl_cor = 172
sl_sag = 115

#%%

if view == 'axi':
    jrange = range_axi
    axis = 0
    sl = sl_axi
elif view == 'cor':
    jrange = range_cor
    sl = sl_cor
    axis = 2
elif view == 'sag':
    jrange = range_sag
    axis = 1
    sl = sl_sag


for i in range(len(tpts)):

    tpt = tpts[i]

    x_img = sitk.ReadImage('template_' + tpt + '_sym_looseMasked.nii.gz')
    x = sitk.GetArrayFromImage(x_img)

    x = np.take(x, sl, axis=axis)[jrange[0][0]:jrange[0][1],jrange[1][0]:jrange[1][1]]
    if view == 'axi': x = np.flipud(np.rot90(x))
    elif view == 'cor': x = np.flipud(x)
    elif view == 'sag': x = np.flipud(np.fliplr(x))

    h, w = x.shape
    fig = plt.figure(figsize=(w, h), dpi=1)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.imshow(x, interpolation='nearest', cmap='gray', vmin=0, vmax=vmax, origin='lower')
    ax.axis('off')
    plt.savefig('imgs/img_' + tpt + '_' + view + '.png', dpi=1, pad_inches=0)
    plt.show()
