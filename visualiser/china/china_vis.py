import sys
import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shapereader
import cartopy.feature as cfeature
import matplotlib
if sys.platform == "darwin":
    matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import pylab


map = plt.subplot(projection=ccrs.Mercator())

outcome = {'Anhui': 1, 'Beijing': 2, 'Chongqing': 2, 'Fujian': 3, 'Guangdong': 1, 'Gansu': 4, 'Guangxi': 2, 'Guizhou': 4, 'Henan': 2, 'Hubei': 4, 'Hebei': 1, 'Heilongjiang': 1, 'Hunan': 3, 'Jilin': 4, 'Jiangsu': 2, 'Jiangxi': 2, 'Liaoning': 3, 'Nei Mongol': 2, 'Ningxia Hui': 1, 'Qinghai': 2, 'Sichuan': 1, 'Shandong': 4, 'Shanghai': 3, 'Shaanxi': 3, 'Shanxi': 4, 'Tianjin': 3, 'Xinjiang Uygur': 3, 'Yunnan': 3, 'Zhejiang': 4, 'Xizang': 4, 'Hainan': 1}

def map_china_visualisation(ax, extent=(70, 160, 5, 50), **kwargs):

    shapefile = 'CHN_adm1.shp'

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

    plt.title('China')
    plt.legend(handles=[senderA, senderB, senderC, senderD, senderE])
    # pylab.savefig('results/chinamap.png')
    plt.show()


map_china_visualisation(map, transform=ccrs.PlateCarree())
