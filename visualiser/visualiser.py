import sys
sys.path.append(r"C:\Users\Windows\Anaconda3\Lib\site-packages")
from cartopy.io import shapereader
import cartopy.crs as ccrs
import matplotlib.pyplot as plt


def visualize_provinces(provinces):

    # maak groepen van kleuren en provincies
    colors = ['Red', 'Yellow', 'Green', 'Orange', 'Blue', 'Grey', 'Pink']
    sender_groups = []
    for i in range(7):
        sender_groups.append([])

    # gooi provincies in groepen op basis van hun zender
    for province in provinces:
        sender_groups[provinces[province].sender.type - 1].append(provinces[province].name)

    kw = dict(resolution='50m', category='cultural', name='admin_1_states_provinces')

    # import state shape reader
    states_shp = shapereader.natural_earth(**kw)
    shp = shapereader.Reader(states_shp)

    # geen idee
    subplot_kw = dict(projection=ccrs.PlateCarree())

    # afmetingen van figuur
    fig, ax = plt.subplots(figsize=(7, 11),
                           subplot_kw=subplot_kw)

    # laat achtergrond zien
    ax.background_patch.set_visible(True)
    ax.outline_patch.set_visible(True)

    # kijk of naam van staat voorkomt in shapefile sate
    for record, state in zip(shp.records(), shp.geometries()):
        name = record.attributes['name']

        # dit maakt grenzen onzichtbaar tenzij ze in de kleurengroep voorkomen
        edgecolor= 'White'
        facecolor = "White"
        for group in range(len(sender_groups)):
            if name in sender_groups[group]:
                facecolor = colors[group]
                break

        # hiermee worden grenzen en kleuren getekend
        ax.add_geometries([state], ccrs.PlateCarree(), facecolor=facecolor, edgecolor=edgecolor )

        # maximale x-coordination -180, 180 en y-coordination -90, 90
        ax.set_extent([-180, -60, 20, 90])
    plt.show()
