import datetime, os

url="http://ftp.cptec.inpe.br/modelos/tempo/WRF/ams_07km/brutos"
file_initial_name = "WRF_cpt_07KM_"

dirpath = os.getcwd()
download_dir = (dirpath+"/Download")
ConvertToNetcdf_dir = (dirpath+"/ConvertToNetcdf")
ConvertToHdf5_dir = (dirpath+"/ConvertToHdf5")
backup_path =	(dirpath+"/Backup")

forecast_mode = 1
#Número de dias a partir da data atual se forecast_mode = 0
number_of_runs = 2

#Data de início e fim se forecast_mode = 0
start = datetime.date(2022,11,24)
end = datetime.date(2022,11,25)

download = 1
#Tempo de espera para uma nova tentativa de download do arquivo (em segundos)
wait_time = 300
#Tempo de espera total em s para o download do arquivo (em segundos) 
wait_total_time = 1800
#Tamanho mínimo do arquivo em bits
min_file_size = 3000000


ConvertToHdf5 = 1

telegram_messages = 0
TOKEN = "YOUR TELEGRAM BOT TOKEN"
chat_id = "YOUR CHAT ID"

#Apaga arquivos grib2 antigos da pasta download_dir
remove_old_files = 0
days_to_remove = 7
