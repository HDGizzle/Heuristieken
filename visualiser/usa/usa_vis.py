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

map = plt.subplot(projection=ccrs.Mercator())

outcome = {'Alabama': 1, 'Alaska': 1, 'Arizona': 4, 'Arkansas': 1, 'California': 2, 'Colorado': 2, 'Connecticut': 4, 'Delaware': 1, 'Florida': 3, 'Georgia': 2, 'Hawaii': 1, 'Idaho': 2, 'Illinois': 3, 'Indiana': 2, 'Iowa': 4, 'Kansas': 4, 'Kentucky': 4, 'Louisiana': 3, 'Maine': 2, 'Maryland': 3, 'Massachusetts': 2, 'Michigan': 4, 'Minnesota': 3, 'Mississippi': 2, 'Missouri': 2, 'Montana': 3, 'Nebraska': 3, 'Nevada': 1, 'New Hampshire': 1, 'New Jersey': 2, 'New Mexico': 1, 'New York': 1, 'North Carolina': 4, 'North Dakota': 2, 'Ohio': 3, 'Oklahoma': 3, 'Oregon': 4, 'Pennsylvania': 4, 'Rhode Island': 3, 'South Carolina': 3, 'South Dakota': 1, 'Tennessee': 3, 'Texas': 4, 'Utah': 3, 'Vermont': 4, 'Virginia': 2, 'Washington': 1, 'West Virginia': 1, 'Wisconsin': 2, 'Wyoming': 4}


def map_usa_visualisation(ax, extent=(-125, -66.5, 20, 55), **kwargs):

    shapefile = 'ne_110m_admin_1_states_provinces.shp'

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
        ax.add_geometries(adm1_shapes[i], ccrs.PlateCarree(),
        facecolor=colors[outcome.get(province.attributes['name_en'])],
        edgecolor="black")

    senderA = mpatches.Patch(color='#377eb8', label='Sender type A')
    senderB = mpatches.Patch(color='#4daf4a', label='Sender type B')
    senderC = mpatches.Patch(color='#984ea3', label='Sender type C')
    senderD = mpatches.Patch(color='#ff7f00', label='Sender type D')
    senderE = mpatches.Patch(color='#e41a1c', label='Sender type E')

    plt.title('USA')
    plt.legend(handles=[senderA, senderB, senderC, senderD, senderE])
    # pylab.savefig('results/usamap.png')
    plt.show()


map_usa_visualisation(map, transform=ccrs.PlateCarree())
