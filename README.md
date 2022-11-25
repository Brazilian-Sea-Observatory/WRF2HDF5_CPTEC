# WRF2HDF5_CPTEC
Tool to download and/or convert WRF files from CPTEC/INPE to HDF5 MOHID format.

Requirements for Linux:
* Python 3
* wgib2 (https://anaconda.org/conda-forge/wgrib2)
* grib files and their wgrib inventory on an http server
* get_inv.pl
* get_grib.pl


Requirements for Windows:
* Python 3
* perl (http://strawberryperl.com/)
* grep (https://sourceforge.net/projects/getgnuwin32/?source=typ_redirect)
* cURL (https://curl.haxx.se/download.html)
* grib files and their wgrib inventory on an http server
* get_inv.pl
* get_grib.pl

You need to comment/uncomment lines in WRF2HDF5_CPTEC.py and WRF_Convert2Netcdf.py depending on your operating system.

You need to compile ConvertToHDF5 to run in Linux (https://github.com/Mohid-Water-Modelling-System/Mohid/tree/master/Solutions/mohid-in-linux).

You need to create a bot and get a Token in order toreceive error messages in Telegram.

Define your directories and inputs in Input_WRF2HDF5_CPTEC.py.
