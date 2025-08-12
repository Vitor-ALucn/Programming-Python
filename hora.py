hour = int(input("Hora de inicio (horas): "))
mins = int(input("Hora de inicio (minutos): "))
dura = int(input("Duração do evento (minutos): "))

hour += (mins + dura) // 60
hour %= 24
mins =  mins = dura % 60

print(hour, mins, sep="")