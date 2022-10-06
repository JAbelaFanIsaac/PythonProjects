from datetime import date
StartYear = int(input("Start year"))
StartMonth = int(input("Start month"))
StartDay = int(input("Start day"))
EndYear = int(input("End year"))
EndMonth = int(input("End month"))
EndDay = int(input("End day"))
StartTime = date(StartYear, StartMonth, StartDay)
EndTime = date(EndYear, EndMonth, EndDay)
Diference = EndTime - StartTime
print(Diference.days)