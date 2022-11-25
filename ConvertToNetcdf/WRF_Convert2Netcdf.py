import subprocess
import glob

files = glob.glob("*.grib2")
files.sort()
outputname = "wrf.nc"

for filename in files:
   
    #Linux
    subprocess.run('wgrib2 -append -match ":TMP:2 m above" ' + filename +  ' -netcdf ' + outputname, shell=True)
    subprocess.run ('wgrib2 -append -match ":UGRD:10 m above" ' + filename +  ' -netcdf ' + outputname, shell=True)
    subprocess.run('wgrib2 -append -match ":VGRD:10 m above" ' + filename +  ' -netcdf ' + outputname, shell=True)
    subprocess.run ('wgrib2 -append -match ":RH:2 m above" ' + filename +  ' -netcdf ' + outputname, shell=True)
    subprocess.run ('wgrib2 -append -match ":PRMSL:" ' + filename +  ' -netcdf ' + outputname, shell=True)
    subprocess.run ('wgrib2 -append -match ":LAND:" ' + filename +  ' -netcdf ' + outputname, shell=True)
    subprocess.run('wgrib2 -append -match ":TCDC:entire atmosphere" ' + filename +  ' -netcdf ' + outputname, shell=True)
    subprocess.run ('wgrib2 -append -match ":DLWRF:surface" ' + filename +  ' -netcdf ' + outputname, shell=True)
    subprocess.run ('wgrib2 -append -match ":DSWRF:surface" ' + filename +  ' -netcdf ' + outputname, shell=True)
    subprocess.run ('wgrib2 -append -match ":HPBL:surface" ' + filename +  ' -netcdf ' + outputname, shell=True)
    subprocess.run ('wgrib2 -append -match ":ALBDO:surface" ' + filename +  ' -netcdf ' + outputname, shell=True)

    #Windows
   # subprocess.run('wgrib2 -append -match ":TMP:2 m above" ' + filename +  ' -netcdf ' + outputname)
   # subprocess.run ('wgrib2 -append -match ":UGRD:10 m above" ' + filename +  ' -netcdf ' + outputname)
   # subprocess.run('wgrib2 -append -match ":VGRD:10 m above" ' + filename +  ' -netcdf ' + outputname)
   # subprocess.run ('wgrib2 -append -match ":RH:2 m above" ' + filename +  ' -netcdf ' + outputname)
   # subprocess.run ('wgrib2 -append -match ":PRMSL:" ' + filename +  ' -netcdf ' + outputname)
   # subprocess.run ('wgrib2 -append -match ":LAND:" ' + filename +  ' -netcdf ' + outputname)
   # subprocess.run('wgrib2 -append -match ":TCDC:entire atmosphere" ' + filename +  ' -netcdf ' + outputname)
   # subprocess.run ('wgrib2 -append -match ":DLWRF:surface" ' + filename +  ' -netcdf ' + outputname)
   # subprocess.run ('wgrib2 -append -match ":DSWRF:surface" ' + filename +  ' -netcdf ' + outputname)
   # #file.write ('wgrib2 -append -match ":PRATE:surface" ' + filename +  ' -netcdf ' + outputname)
   # subprocess.run ('wgrib2 -append -match ":HPBL:surface" ' + filename +  ' -netcdf ' + outputname)
   # subprocess.run ('wgrib2 -append -match ":ALBDO:surface" ' + filename +  ' -netcdf ' + outputname)
	 
