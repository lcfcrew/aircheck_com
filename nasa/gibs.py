import requests

import os

import h5py as hdf

from django.conf import settings

from .models import DiscretizedDataPoint

response = requests.get('http://map1.vis.earthdata.nasa.gov/wmts-webmerc/MLS_N2O_46hPa_Day/default/2014-04-09/GoogleMapsCompatible_Level6/1/1/1.png')
'''
for nasa_data_file in nasa_data_files:
    file_path = os.path.join(settings.PROJECT_ROOT + settings.MEDIA_URL, nasa_data_file.hdf.name)
    infile = hdf.File(file_path, "r")

    print(infile['HDFEOS'].keys())

    #print(infile.keys())

    for key in infile['HDFEOS'].keys():
        print(key)
        print('===')
        for key2 in infile['HDFEOS'][key].keys():
            print(key2)
            print('---')
            for key3 in infile['HDFEOS'][key][key2].keys():
                print(key3)

    #for name in infile:
    #    print(name)

    break
'''
