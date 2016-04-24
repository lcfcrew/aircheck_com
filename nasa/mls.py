from ftplib import FTP
import os
from StringIO import StringIO
import xml.etree.ElementTree as ET

from django.conf import settings
from django.core.files.base import File

from .models import NasaDataFile


#host = 'discnrt1.gesdisc.eosdis.nasa.gov'
host = 'omisips1.omisips.eosdis.nasa.gov'

ftp = FTP(host)     # connect to host, default port
ftp.login('cdelguercio', 'FAkbymFopsE5')                     # user anonymous, passwd anonymous@

#ftp.cwd('data/Aura_NRT/ML2CO_NRT.003/Recent/')               # change into "Recent" directory
ftp.cwd('OMSO2NRTb/')

filenames = ftp.nlst()

#print(filenames)    # list directory contents

for filename in filenames:
    if filename[-3:] != 'xml':
        try:
            nasa_data_file = NasaDataFile.objects.get(hdf='./' + filename)
        except Exception:
            nasa_data_file = NasaDataFile()
            print(filename)
            s = StringIO()
            ftp.retrbinary("RETR " + filename, s.write)
            s.size = s.tell()
            nasa_data_file.hdf.save(filename, File(s))

        if nasa_data_file.xml.name == '' or not nasa_data_file.xml.name:
            xml_filename = filename + '.xml'
            print(xml_filename)
            s = StringIO()
            ftp.retrbinary("RETR " + xml_filename, s.write)
            s.size = s.tell()
            nasa_data_file.xml.save(xml_filename, File(s))

        # open xml file and read metadata
        file_path = os.path.join(settings.PROJECT_ROOT + settings.MEDIA_URL, nasa_data_file.xml.name)
        tree = ET.parse(file_path)
        root = tree.getroot()

        date = root.findtext('./RangeDateTime/RangeBeginningDate')
        time = root.findtext('./RangeDateTime/RangeBeginningTime')
        print(date)
        print(time)

        nasa_data_file.date = date + 'T' + time

        nasa_data_file.collection_short_name = root.findtext('./CollectionMetaData/ShortName')
        nasa_data_file.collection_long_name = root.findtext('./CollectionMetaData/LongName')
        nasa_data_file.bounding_west = root.findtext('./SpatialDomainContainer/HorizontalSpatialDomainContainer/BoundingRectangle/WestBoundingCoordinate')
        nasa_data_file.bounding_north = root.findtext('./SpatialDomainContainer/HorizontalSpatialDomainContainer/BoundingRectangle/NorthBoundingCoordinate')
        nasa_data_file.bounding_east = root.findtext('./SpatialDomainContainer/HorizontalSpatialDomainContainer/BoundingRectangle/EastBoundingCoordinate')
        nasa_data_file.bounding_south = root.findtext('./SpatialDomainContainer/HorizontalSpatialDomainContainer/BoundingRectangle/SouthBoundingCoordinate')

        nasa_data_file.save()
