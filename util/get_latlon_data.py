import requests
import numpy
#import IPython
from cStringIO import StringIO
from PIL import Image
import colorsys
import datetime
from datetime import timedelta
import numpy as np
import aqi

min_lat = -90.0
max_lat = 90.0
min_lon = -180.0
max_lon = 180.0
height = 256
width = 256

def get_aqi(dust,so2,co):
    query = [(aqi.POLLUTANT_CO_8H,co),
             (aqi.POLLUTANT_PM25,dust),
             (aqi.POLLUTANT_SO2_1H,so2)]
    return aqi.to_aqi(query)

def HSVColor(img):
    if isinstance(img,Image.Image):
        r,g,b,a = img.split()
        Hdat = []
        Sdat = []
        Vdat = [] 
        for rd,gn,bl,al in zip(r.getdata(),g.getdata(),b.getdata(),a.getdata()) :
            h,s,v = colorsys.rgb_to_hsv(rd/255.,gn/255.,bl/255.)
            Hdat.append(int(h*255.))
            Sdat.append(int(s*255.))
            Vdat.append(int(v*255.))
        r.putdata(Hdat)
        g.putdata(Sdat)
        b.putdata(Vdat)
        return Image.merge('RGB',(r,g,b))
    else:
        return None

def get_earth_image(instType="MLS_CO_215hPa_Day",z=1,x=1,y=1,when=datetime.datetime.now()):
    datestr = when.strftime("%Y-%m-%d")
    response = requests.get('http://map1.vis.earthdata.nasa.gov/wmts-webmerc/%s/default/%s/GoogleMapsCompatible_Level6/%d/%d/%d.png' % (instType,datestr,z,x,y))
    from cStringIO import StringIO
    file_pngdata = StringIO(response.content)
    dt = Image.open(file_pngdata).convert("RGBA")
    hsv_img = HSVColor(dt)
    return hsv_img

def get_lat_lon(img):
    lats = np.linspace(min_lat,max_lat,height)
    lons = np.linspace(min_lon,max_lon,width)
    out = []
    for i in range(0,height):
        for j in range(0,width):
            if img.getpixel((j,i))[0] != 0:
                out.append((lats[i],lons[j],img.getpixel((j,i))[0]))    
            
    return out

def get_last_12d(instType="MLS_CO_215hPa_Day"):
    outstuff = []
    for single_date in (datetime.datetime.now() + timedelta(n) for n in range(0,-12,-1)):
        i = get_earth_image(instType=instType,when=single_date)
        outstuff += get_lat_lon(i)
    return outstuff

if __name__ == '__main__':

    print len(get_last_12d())