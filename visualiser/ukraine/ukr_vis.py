import sys
import cartopy.crs as ccrs
import cartopy.io.shapereader as shapereader
import cartopy.feature as cfeature
import matplotlib
if sys.platform == "darwin":
    matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import pylab

outcome = {
    'Cherkasy': 1,
    'Chernihiv': 4,
    'Chernivtsi': 4,
    "Dnipropetrovs'k": 1,
    "Donets'k": 3,
    "Ivano-Frankivs'k": 3,
    'Kharkiv': 2,
    'Kherson': 3,
    "Khmel'nyts'kyy": 2,
    'Kiev': 2,
    'Kirovohrad': 4,
    "Luhans'k": 4,
    "L'viv": 2,
    'Mykolayiv': 2,
    'Odessa': 1,
    'Poltava': 3,
    'Rivne': 3,
    'Sumy': 1,
    "Ternopil'": 1,
    'Vinnytsya': 3,
    'Volyn': 4,
    'Transcarpathia': 1,
    'Zaporizhzhya': 2,
    'Zhytomyr': 4}

map = plt.subplot(projection=ccrs.Mercator())


def map_ukr_visualisation(ax, extent=(20, 45, 50, 65), **kwargs):

    shapefile = 'UKR_adm1.shp'

    reader = shapereader.Reader(shapefile)
    adm1_shapes = list(reader.geometries())
    provinces = reader.records()

    #  A province could never have sendertype 0 so colors[0] would not be used
    #  Therefore this color is set to None.
    #           None         blue       green     purple    orange
    colors = [None, '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

    ax.plot(60, 56, 'r*', ms=20, **kwargs)
    ax.set_extent(extent)
    ax.coastlines(resolution='50m')
    ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=.5)
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.STATES)
    ax.add_feature(cfeature.OCEAN)
    for i in range(len(adm1_shapes)):
        province = next(provinces)
        state = province.attributes['NAME_1']
        if outcome.get(state) == None:
            ax.add_geometries(adm1_shapes[i], ccrs.PlateCarree(),
            facecolor="#d6d6c2",
            edgecolor="black")
        else:
            ax.add_geometries(adm1_shapes[i], ccrs.PlateCarree(),
            facecolor=colors[outcome.get(state)],
            edgecolor="black")

    senderA = mpatches.Patch(color='#377eb8', label='Sender type A')
    senderB = mpatches.Patch(color='#4daf4a', label='Sender type B')
    senderC = mpatches.Patch(color='#984ea3', label='Sender type C')
    senderD = mpatches.Patch(color='#ff7f00', label='Sender type D')
    senderE = mpatches.Patch(color='#e41a1c', label='Sender type E')

    plt.title('Ukraine')
    plt.legend(handles=[senderA, senderB, senderC, senderD, senderE])
    plt.show()
    # pylab.savefig('results/ukrainemap.png')


map_ukr_visualisation(map, transform=ccrs.PlateCarree())
