import os

import h5py as hdf

from django.conf import settings

from .models import NasaDataFile

nasa_data_files = NasaDataFile.objects.all()

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
