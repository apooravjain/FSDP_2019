days=input("enter the days").split(",")
print(days)
count=0
for item in days:
    count+=1
if count==7:
    print("all days are present")
else:
    w=7-count
    print(str(w)+"days are missing")
days=('Monday', 'Wednesday', 'Thursday', 'Saturday')
missing_days=('Tusday','Friday','Sunday')
all_days=days[0]+missing_days[0]+days[1]+days[2]+missing_days[1]+days[3]+missing_days[2]
print(all_days)