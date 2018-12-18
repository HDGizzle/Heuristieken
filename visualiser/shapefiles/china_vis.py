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


def mapplotterCHINA(benchmark):

    map = plt.subplot(projection=ccrs.Mercator())

    def map_china_visualisation(ax):

        shapefile = 'CHN_adm1.shp'

        reader = shapereader.Reader(shapefile)
        adm1_shapes = list(reader.geometries())
        provinces = reader.records()

        #  A province could never have sendertype 0 so colors[0] would not be used
        #  Therefore this color is set to None.
        #         None     blue       green     purple    orange        red
        colors = [None, '#377eb8', '#4daf4a', '#984ea3', '#ff7f00', '#e41a1c']

        ax.set_extent([70, 160, 5, 50])
        ax.coastlines(resolution='50m')
        ax.add_feature(cfeature.BORDERS, linestyle='-', alpha=.5)
        ax.add_feature(cfeature.LAND)
        ax.add_feature(cfeature.STATES)
        ax.add_feature(cfeature.OCEAN)
        for i in range(len(adm1_shapes)):
            province = next(provinces)
            state = province.attributes['NAME_1']
            if benchmark.get(state) is None:
                ax.add_geometries(adm1_shapes[i], ccrs.PlateCarree(),
                facecolor="#d6d6c2",
                edgecolor="black")
            else:
                ax.add_geometries(adm1_shapes[i], ccrs.PlateCarree(),
                facecolor=colors[benchmark.get(state)],
                edgecolor="black")

        senderA = mpatches.Patch(color='#377eb8', label='Sender type A')
        senderB = mpatches.Patch(color='#4daf4a', label='Sender type B')
        senderC = mpatches.Patch(color='#984ea3', label='Sender type C')
        senderD = mpatches.Patch(color='#ff7f00', label='Sender type D')
        senderE = mpatches.Patch(color='#e41a1c', label='Sender type E')

        plt.title('China')
        plt.legend(handles=[senderA, senderB, senderC, senderD, senderE])
        pylab.savefig('results/chinamap.png')

    map_china_visualisation(map)
