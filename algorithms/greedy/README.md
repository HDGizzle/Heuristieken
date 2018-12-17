Welsh Powell Algorithm
=======================

Wellsh Powell wordt gebruikt als algoritme voor het vinden van oplossingen van kleurenproblemen, welke vergelijk is met Radio Russia.
Wellsh Powell is een greedy algoritme en deelt per zender eerst landen toe met de meeste verbindingen. Het algoritme is gebaseerd op de volgende stappen

1. Kijk naar het aantal verbindingen/aangelegen provincies per provincie
2. Sorteer de provincies gebaseerd op het aantal verbindingen
3. Per zender plaats het betreffende type in de eerstmogelijke provincie met het meeste verbindingen
4. Ga verder met de volgende provincies met de meeste verbindingen welke nog niet grenst aan een provincie met het huidige zendertype en  plaats de zender. Verwijder vervolgens de provincie uit de lijst.
5. Herhaal het proces met alle andere zendertypes totdat alle provincies een zender toebedeeld hebben gekregen
(http://mrsleblancsmath.pbworks.com/w/file/fetch/46119304/vertex%20coloring%20algorithm.pdf)
