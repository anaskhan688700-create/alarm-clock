from determine import determine
from playsound import playsound

alarm =  input("Enter alarm  you want to set (HHMMSS):")
alarm_hours  = alarm[0:2]
alarm_minutes = alarm[2:4]
alarm_seconds = alarm[4:6]
while true:
    now = datetime.now()
    current_hours = now.strftime("%h")
    current_minutes = now.strftime("%m")
    current_seconds = now.strftime("%s")
    current_period = now.strftime("%p")
    if alarm_period == current_period:
        if alarm_second ==current_seconds:
            if alarm_minutes == current_minutes:
                if alarm_hours == current_hours:
                    print("Wake Up")
                    playsound("rockstar.flac")
                    break