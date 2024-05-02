from datetime import datetime,timedelta

data = datetime.now()
data_str = '2023-10-20 10:20'
mascara_ptbr = '%d/%m/%Y'
mascara_en = '%Y-%m-%d %H:%M'

print(data.strftime(mascara_ptbr))
print(datetime.strptime(data_str,mascara_en))