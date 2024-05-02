import pytz
from datetime import datetime

d =  datetime.now(pytz.timezone('Europe/Oslo'))
dt = datetime.now(pytz.timezone('America/Sao_Paulo'))
d1= datetime.now(pytz.timezone('America/New_York'))
da = datetime.now(pytz.timezone('Asia/Tokyo'))

print(d,'\n',dt,'\n',d1,'\n',da)