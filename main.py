# Explained: inactiveMinutes = (hours * 60) + minutes
inactiveMinutes = (0 * 60) + 0

# Hardly modified
minutesAYear = 60 * 24 * 365

inactivity = (inactiveMinutes * 100) / minutesAYear
sla = ((minutesAYear - inactiveMinutes) * 100 ) / minutesAYear

print("[#########################################]\n")

print("(" + str(inactiveMinutes) + " * 100) / " + str(minutesAYear) + " = " + str(round(inactivity, 3)) + "% d'inactivitat")
print("Inactivitat = " + str(round(inactivity, 3)) + "%")

print("\n[#########################################]\n")

print("((" + str(minutesAYear) + " - " + str(inactiveMinutes) + ") * 100) / " + str(minutesAYear) + " = " + str(round(sla, 3)) + "% d'activitat (SLA)")
print("SLA = " + str(round(sla, 3)) + "%")

# Repository
# https://github.com/TheMineWayEstudis/SLA