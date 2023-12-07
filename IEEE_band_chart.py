#%%
import numpy as np
from matplotlib import pyplot as plt
def set_font(fontsize=18, font="Times New Roman"):
    rc = {"font.size" : fontsize,
    "font.family" : font,
    "mathtext.fontset" : "stix"}
    plt.rcParams.update(rc)
set_font(fontsize=15)

bandnames = ['L', 'S', 'C', 'X', 'Ku', 'K', 'Ka', 'V', 'W', 'mm']
bandlimits = np.array([[1, 2],
                    [2, 4],
                    [4, 8],
                    [8, 12],
                    [12, 18],
                    [18, 27],
                    [27, 40],
                    [40, 75],
                    [75, 110],
                    [110, 330]])
bandwidths = bandlimits[:,1] - bandlimits[:,0]
centers = np.mean(bandlimits, axis=1)-np.array([0.1, 0.3, 0.4, 0.4, .8, 1.2, 1.2, 4, 3, 30])

bandlimits_log = np.log10(bandlimits)
bandwidths_log = bandlimits_log[:,1] - bandlimits_log[:,0]
centers_log = np.mean(bandlimits_log, axis=1)

prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']

vlines = np.array([13.8, 94, 35.5])

#%%
y = 0.5

fig, ax = plt.subplots(1, 1, figsize=(10,4))
ax.barh(y*np.ones(len(bandnames)), 
         bandwidths,
         left=bandlimits[:,0],
         color=colors,
         log=True)
for i, label in enumerate(bandnames):
    ax.text(centers[i], y+.1, label, ha='center')
    ax.text(centers[i], y-.1, f'{bandlimits[i,0]} - {bandlimits[i,1]}', fontsize=10, ha='center')
ax.hlines(0.201, np.amin(bandlimits), np.amax(bandlimits), color='black', linewidth=1)
ax.set_ylim(0.2, 2.8)
ax.set(yticklabels=[])
ax.set_xlim(1, np.amax(bandlimits))
ax.set_xlabel('GHz')
plt.tick_params(
    axis='y',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    left=False,      # ticks along the bottom edge are off
    right=False)         # ticks along the top edge are off # labels along the bottom edge are off
plt.box(on=False)
plt.show()


# %%
