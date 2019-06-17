

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt 
import json

with open('bp_gps_locations.json','r') as f:
	bps = json.load(f)

print(json.dumps(bps))


# top21 = dict( bp for bp in bps.key if bp['rank']<5) 

print(bps.keys())
top21 = {}

top21 = [ bps[key] for key in bps.keys() if bps[key]['rank'] <  22 and bps[key]['lat'] != 'NULL']
bot21 = [ bps[key] for key in bps.keys() if bps[key]['rank'] >= 22 and bps[key]['lat'] != 'NULL']
print(top21)
print(bot21)

# plot the BPs locations
# m = Basemap(projection='robin',lon_0=0,resolution='c')
plt.figure(figsize=(12,12))
m = Basemap(projection='robin',lon_0=0)
m.bluemarble()
markersize = 15

# plot top 21 in red
lats = [bp['lat'] for bp in top21]
lons = [bp['lon'] for bp in top21]
x, y = m(lons,lats)
m.scatter(x,y,markersize,marker='o',color='r',label='Top 21 BPs')

# plot bottom 21 in blue
plt.title('EOS Block Producers by Location')
plt.legend()
plt.savefig('fig/bp_gps_locations_top21.png')
plt.show()
