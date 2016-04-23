import os

import h5py as hdf

from django.conf import settings

from .models import NasaDataFile

nasa_data_files = NasaDataFile.objects.all()

for nasa_data_file in nasa_data_files:
    file_path = os.path.join(settings.PROJECT_ROOT + settings.MEDIA_URL, nasa_data_file.hdf.name)
    infile = hdf.File(file_path, "r")

    for name in infile:
        print(name)
