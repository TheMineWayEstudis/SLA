# Calculadora d'SLA
Es tracta d'un conjunt d'scripts de Python que et permeten calcular la disponibilitat donat un SLA o una quantitat de minuts.

## Com fer-lo servir
Si volem calcular l'SLA a partir d'una quantitat de minuts, anem a l'script **fromMinutes.py**:
La variable ```inactiveMinutes``` ha de contenir els minuts d'inactivitat anuals.

Si volem calcular el temps de disponibilitat a partir d'un SLA, anem a l'script **fromSLA.py:
la variable ```sla``` conté un número que representa el percentatge d'SLA (disponibilitat).
