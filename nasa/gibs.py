from .models import DiscretizedDataPoint

from util.get_latlon_data import get_last_12d

data_points = get_last_12d('MLS_CO_215hPa_Day')
for data_point in data_points:
    dp = DiscretizedDataPoint(type='CO', latitude=data_point[0], longitude=data_point[1], value=float(data_point[2]) * 250./256.)
    dp.save()

data_points = get_last_12d('MLS_SO2_147hPa_Day')
for data_point in data_points:
    dp = DiscretizedDataPoint(type='SO2', latitude=data_point[0], longitude=data_point[1], value=20. + float(data_point[2]) * 180./256.)
    dp.save()

data_points = get_last_12d('AIRS_Dust_Score')
for data_point in data_points:
    dp = DiscretizedDataPoint(type='Dust', latitude=data_point[0], longitude=data_point[1], value=360. + float(data_point[2]) * 140./256.)
    dp.save()

data_points = get_last_12d('MLS_O3_46hPa_Day')
for data_point in data_points:
    dp = DiscretizedDataPoint(type='O3', latitude=data_point[0], longitude=data_point[1], value=0.5 + float(data_point[2]) * 4./256.)
    dp.save()
