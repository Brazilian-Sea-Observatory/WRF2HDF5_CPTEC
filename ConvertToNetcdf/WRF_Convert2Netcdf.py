import subprocess
import glob

input_file = "wgrib2.bat"

files = glob.glob("*.grib2")
#filename1 = files[0] 
outputname = "wrf"
with open(input_file,"w") as file:
	for filename in files:
		subprocess.run('wgrib2 -append -match ":TMP:2 m above" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
		subprocess.run ('wgrib2 -append -match ":UGRD:10 m above" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
		subprocess.run('wgrib2 -append -match ":VGRD:10 m above" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
		subprocess.run ('wgrib2 -append -match ":RH:2 m above" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
		subprocess.run ('wgrib2 -append -match ":PRMSL:" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
		subprocess.run ('wgrib2 -append -match ":LAND:" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
		subprocess.run('wgrib2 -append -match ":TCDC:entire atmosphere" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
		subprocess.run ('wgrib2 -append -match ":DLWRF:surface" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
		subprocess.run ('wgrib2 -append -match ":DSWRF:surface" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
		#file.write ('wgrib2 -append -match ":PRATE:surface" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
		subprocess.run ('wgrib2 -append -match ":HPBL:surface" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
		subprocess.run ('wgrib2 -append -match ":ALBDO:surface" ' + filename +  ' -netcdf ' + outputname +'.nc \n')
	 