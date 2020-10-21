import pygrib as py

# import datetime
# import numpy as np
# grib_path = "/home/ariel/datasets/shanxi/CLDAS/TEMP/2019/20191211/Z_NAFP_C_BABJ_20191211150952_P_CLDAS_RT_CHN_0P05_HOR-TEM-2019121115.GRB2"
grib_path = "/home/gym/datasets/Z_NAFP_C_BABJ_20200305110948_P_CLDAS_RT_CHN_0P05_HOR-TEM-2020030511.GRB2"
path2 = "/home/gym/datasets/yunnan/temperature/scmoc_grib/2020BJ/202003BJ/20200305BJ/Z_NWGD_C_BABJ_20200305030356_P_RFFC_SCMOC-TMP_202003050800_24003.GRB2"

latmin, latmax, lonmin, lonmax = 22.749, 29.751, 101.499, 106.501

grbs = py.open(grib_path)

grbs2 = py.open(path2)

grbs_ = grbs.select(name="2 metre temperature")[0]
print(grbs_)
targetData, lats, lons = grbs_.data(lat1=latmin, lat2=latmax, lon1=lonmin, lon2=lonmax)
print(grbs_.stepRange, targetData.shape, lats.min(), lats.max(), lons.min(), lons.max())

# for grb in grbs:
#     print(grb)
#     print(grb.keys())
#     # print(grb.tablesVersionLatest, grb.tablesVersion, grb.localTablesVersion)
#     # exit()
#     targetData, lats, lons = grb.data(lat1=latmin, lat2=latmax, lon1=lonmin, lon2=lonmax)
#     print(grb.stepRange, targetData.shape, lats.min(), lats.max(), lons.min(), lons.max())
print("-----------------------------------------")
grbs2_ = grbs2.select(name="2 metre temperature")[0]
print(grbs2_)
targetData, lats, lons = grbs2_.data(lat1=latmin, lat2=latmax, lon1=lonmin, lon2=lonmax)
print(grbs2_.stepRange, targetData.shape, lats.min(), lats.max(), lons.min(), lons.max())
# for grb in grbs2_:
#     print(grb)
#     targetData, lats, lons = grb.data(lat1=latmin, lat2=latmax, lon1=lonmin, lon2=lonmax)
#     print(grb.stepRange, targetData.shape, lats.min(), lats.max(), lons.min(), lons.max())
#     tt1 = grb.data(lats)
#     print(grb['forecastTime'])
#     latmin = grb.latitudeOfFirstGridPointInDegrees  # 32.05
#     latmax = grb.latitudeOfLastGridPointInDegrees  # 43.2
#     lonmin = grb.longitudeOfFirstGridPointInDegrees  # 107.7
#     lonmax = grb.longitudeOfLastGridPointInDegrees
#     print(latmin, latmax, lonmin, lonmax)


# if __name__ == '__main__':
#     latmin, latmax, lonmin, lonmax = 22.749, 29.751, 101.499, 106.501
