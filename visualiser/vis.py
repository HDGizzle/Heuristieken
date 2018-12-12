import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shapereader
import cartopy.feature as cfeature
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import shapefile


fname = 'ne_110m_admin_1_states_provinces.shp'
# states_shp = shapereader.natural_earth(resolution='110m',
#                                      category='cultural', name=fname)

reader = shapereader.Reader(fname)
adm1_shapes = list(reader.geometries())
# province = reader.records()

mypt = (60, 56)

projection = ccrs.Mercator()
ax1bis = plt.subplot(projection=ccrs.Mercator())

#           Red         blue       green     purple    orange
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3', '#ff7f00']

def plotpt(ax, extent=(-125, -66.5, 20, 50), **kwargs):

    ax.plot(mypt[0], mypt[1], 'r*', ms=20, **kwargs)
    ax.set_extent(extent)
    ax.coastlines(resolution='50m')
    ax.add_feature(cartopy.feature.BORDERS, linestyle='-', alpha=.5)
    ax.add_feature(cartopy.feature.LAND)
    ax.add_feature(cartopy.feature.STATES)
    # ax.add_feature(states_provinces, edgecolor='gray')
    for i in range(len(adm1_shapes)):
        ax.add_geometries(adm1_shapes[i], ccrs.PlateCarree(), facecolor=colors[i%5], edgecolor ="black")

    # facecolor should be depending on the sender type

    # for country
    # for province in adm1_shapes:
    #     ax.add_geometries([province], projection,
    #         facecolor=cm.jet(np.random.random(1)), edgecolor='k')



    plt.title('USA')


plotpt(ax1bis, transform=ccrs.PlateCarree())


plt.show()



# for state in shapereader.Reader(fname).geometries():
#     facecolor = [0.9375, 0.9375, 0.859375]
#     edgecolor = 'black'
#
#     if province_sender == 1:
#             facecolor = 'red'
#     if province_sender == 2:
#             facecolor = 'blue'
#     if province_sender == 3:
#             facecolor = 'yellow'
#     if province_sender == 4:
#             facecolor = 'green'
#     if province_sender == 5:
#             facecolor = 'purple'
