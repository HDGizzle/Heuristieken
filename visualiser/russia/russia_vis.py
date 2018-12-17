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

outcome = {'Belgorod': 1, 'Bryansk': 3, 'Vladimir': 1, 'Voronezh': 3, 'Ivanovo': 3, 'Kaluga': 1, 'Kostroma': 1, 'Kursk': 2, 'Lipetsk': 1, 'Moskva': 2, 'Orel': 4, "Ryazan'": 4, 'Smolensk': 4, 'Tambov': 2, "Tver'": 3, 'Tula': 3, "Yaroslavl'": 4, 'Karelia': 3, 'Komi': 2, "Arkhangel'sk": 4, 'Vologda': 2, 'Kaliningrad': 1, 'Leningrad': 1, 'Murmansk': 4, 'Novgorod': 4, 'Pskov': 2, 'City of St. Petersburg': 2, 'Nenets': 3, 'Bashkortostan': 3, 'Mariy-El': 4, 'Mordovia': 1, 'Tatarstan': 1, 'Udmurt': 2, 'Chuvash': 3, "Perm'": 4, 'Kirov': 3, 'Nizhegorod': 2, 'Orenburg': 2, 'Penza': 3, 'Samara': 3, 'Saratov': 1, "Ul'yanovsk": 2, 'Adygey': 4, 'Kalmyk': 3, 'Krasnodar': 3, "Astrakhan'": 1, 'Volgograd': 2, 'Rostov': 1, 'Dagestan': 1, 'Ingush': 4, 'Kabardin-Balkar': 1, 'Karachay-Cherkess': 2, 'North Ossetia': 2, 'Chechnya': 3, "Stavropol'": 4, 'Kurgan': 3, 'Sverdlovsk': 1, "Tyumen'": 4, 'Chelyabinsk': 4, 'Khanty-Mansiy': 3, 'Yamal-Nenets': 1, 'Gorno-Altay': 4, 'Buryat': 2, 'Tuva': 3, 'Khakass': 2, 'Altay': 2, "Zabaykal'ye": 4, 'Krasnoyarsk': 4, 'Irkutsk': 1, 'Kemerovo': 1, 'Novosibirsk': 4, 'Omsk': 1, 'Tomsk': 2, 'Sakha': 2, 'Kamchatka': 1, "Primor'ye": 1, 'Amur': 3, 'Maga Buryatdan': 3, 'Sakhalin': 4, 'Yevrey': 2, 'Chukot': 4}

map = plt.subplot(projection=ccrs.Mercator())


def map_russia_visualisation(ax, extent=(25, 180, 80, 40), **kwargs):

    shapefile = 'RUS_adm1.shp'
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

    plt.title('Russia')
    plt.legend(handles=[senderA, senderB, senderC, senderD, senderE])
    plt.show()
    pylab.savefig('results/russiamap.png')


map_russia_visualisation(map, transform=ccrs.PlateCarree())
