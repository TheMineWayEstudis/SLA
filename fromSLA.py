sla = 100 # SLA

# Hardly modified
minutesAYear = 60 * 24 * 365

minutes = (sla * minutesAYear) / 100

operation = "(" + str(sla) + " * " + str(minutesAYear) + ") / 100"

print(operation + " = " + str(minutes) + " minuts d'activitat")
print(operation + " = " + str(minutes) + " / 60 = " + str(minutes / 60) + " hores d'activitat")