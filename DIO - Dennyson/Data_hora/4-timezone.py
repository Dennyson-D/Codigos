from datetime import datetime,timezone,timedelta

dt_oslo =  datetime.now(timezone(timedelta(hours=2)))
dt_sp = datetime.now(timezone(timedelta(hours=-3),'BR'))


print(dt_oslo,'\n',dt_sp)