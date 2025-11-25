from datetime import datetime
input_time = input()
input_time_obj = datetime.strptime(input_time, "%H:%M")
hour=input_time_obj.hour
minute=input_time_obj.minute
a=hour-12
if a<0:
    print(f"Only {hour:02}:{minute:02}.  Too early to Dang.")
elif a>0 and minute>0:
    for i in range(1,a+2):
     print("Dang",end="")
elif a>0 and minute==0:
    for i in range(1,a+1):
        print("Dang",end="")
elif a==0 and minute>0:
        print("Dang",end="")
elif a==0 and minute==0:
    print(f"Only {hour:02}:{minute:02}.  Too early to Dang.")