State Space
===========

Deze file bevat 3 objectieve functies voor het bepalen van de minimale en maximale zendertypes nodig en het vinden van kostengrenzen. Daarnaast wordt er een beschrijving gegeven van de omvang van de state space en de bounds van kosten en zendergebruik voor de uitkomsten

## Objectieve functie clusters:
De maximale hoeveelheid provincies in een cluster (een cluster is een groep provincies die allemaal aan elkaar grenzen)
bepaalt hoeveel zenders er minimaal nodig zijn om de kaart in te vullen om dat alle provincies in deze groep ieder
een unieke zender toegewezen moet krijgen.

Objectieve functie gemiddelde hoeveelheid clusters https://nl.wikipedia.org/wiki/Vierkleurenstelling:
Volgens de vierkleurenstelling is het niet mogelijk om een kaart te vinden waar meer dan vier kleuren nodig zijn
om een kaart in te vullen waar alle buren een verschillende kleur moeten hebben, omdat de gemiddelde hoeveelheid
buren voor elk vlak nooit op vijf uit kan komen. Aangezien we voorbeelden hebben gevonden waar landen met clusters
van maximaal drie provincies voor alsnog niet met vier kleuren ingevuld konden worden hebben we deze functie toegevoegd.
Landen waar het niet lukte hadden alsnog een gemiddelde van 3.8 buren per provincie, wat een verklaring kan geven

## State space:
Elke provincie kan een van zeven zendertypes toebedeeld krijgen. Dat maakt de hoeveelheid mogelijkheden per provincie 7
Als in elke provincie 7 verschillende zenders geplaatst kunnen worden zijn er onder relaxte vereisten 7 tot de macht
van het aantal provincies aan mogelijkheden.

De state space voor alle landen is als volgt:
Oekraine: 1.9158123e+20
Verenigde Staten: 1.798465e+42
Rusland: 1.9862746e+69
China: 5.4116956e+28

## Bounds voor zendertypes:
De lower en upper bounds van het aantal mogelijke zenders kan als volgt worden berekend:
Allereerst aan de hand van de hoeveelheid gelijktijdige verbindingen tussen buren, hoeveel buren zijn er maximaal tegelijkertijd buren van elkaar. Hiervoor wordt de clusterfunctie gebruikt. De maximale omvang van een cluster wordt gebruik als lower bound voor de objective function.

Minimaal aantal benodigde zendertypes volgens clusters:
Oekraïne: 3
Verenigde Staten: 4
Rusland: 3
China: 3

Het gemiddelde aantal verbindingen speelt volgens de vierkleurentheorie echter ook een rol en daarom is voor alle landen hier onder het gemiddelde aantal buren weergegeven. Opvallend is namelijk dat wij voor geen bovenstaande landen met een omvang van 3 landen maximaal in een cluster geen driezenderoplossing hebben kunnen vinden:

Gemiddeld aantal buren per land:
Oekraïne: 4.25
Verenigde Staten: 4.4
Rusland: 4.5
China: 3.9

Er kan worden geconcludeerd dat clusters alleen niet voldoende verklarend is en het gemiddeld aantal connecties ook een rol speelt. Voor alle landen op China na is het gemiddeld aantal connecties ook hoger dan vier. Dit suggereert dat er wellicht alleen voor China een driezenderoplossing gevonden kan worden.

De upperbound voor alle vier de landen is hetzelfde, alle zeven zendertypes worden dan gebruikt.
Oekraïne: 7
Verenigde Staten: 7
Rusland: 7
China: 7

## Bounds voor kosten:
De bounds voor kostenuitkomsten zijn berekend onder relaxte constraints, namelijk dat aan elkaar grenzende provincies wel hetzelfde zendertype mogen gebruiken. De goedkoopste uitkomst is dan dat in elke provincie zendertype "A" uit kostenschema 4 wordt gebruikt en de duurste uitkomst gebruikt in elke provincie zendertype "G" uit kostenschema 4.

Lowerbound:
Oekraïne: 72
Verenigde Staten: 150
Rusland: 243
China: 102

Upperbound:
Oekraïne: 1392
Verenigde Staten: 2900
Rusland: 4698
China: 1972
