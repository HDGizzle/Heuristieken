State Space
===========

Deze file bevat 3 objectieve functies voor het bepalen van de minimale en maximale zendertypes nodig en het vinden van kostengrenzen

Objectieve functie clusters: 
De maximale hoeveelheid provincies in een cluster (een cluster is een groep provincies die allemaal aan elkaar grenzen)
bepaalt hoeveel zenders er minimaal nodig zijn om de kaart in te vullen om dat alle provincies in deze groep ieder
een unieke zender toegewezen moet krijgen.

Objectieve functie gemiddelde hoeveelheid clusters https://nl.wikipedia.org/wiki/Vierkleurenstelling:
Volgens de vierkleurenstelling is het niet mogelijk om een kaart te vinden waar meer dan vier kleuren nodig zijn
om een kaart in te vullen waar alle buren een verschillende kleur moeten hebben, omdat de gemiddelde hoeveelheid
buren voor elk vlak nooit op vijf uit kan komen. Aangezien we voorbeelden hebben gevonden waar landen met clusters
van maximaal drie provincies voor alsnog niet met vier kleuren ingevuld konden worden hebben we deze functie toegevoegd.
Landen waar het niet lukte hadden alsnog een gemiddelde van 3.8 buren per provincie, wat een verklaring kan geven

State space:
Elke provincie kan een van zeven zendertypes toebedeeld krijgen. Dat maakt de hoeveelheid mogelijkheden per provincie 7
Als in elke provincie 7 verschillende zenders geplaatst kunnen worden zijn er onder relaxte vereisten 7 tot de macht
van het aantal provincies aan mogelijkheden.

