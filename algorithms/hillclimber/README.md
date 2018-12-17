Hill climber
=====================

Hill climber gebruikt een gegeven input en krijgt een limiet van N keer om de
map te bekijken en veranderingen door te voeren. Als de functie binnen N keer
een uitkomst weet te vinden, wordt deze de uitkomst aangenomen als nieuwe benchmark
en wordt de functie opnieuw aangeroepen. Als er geen betere uitkomst binnen de
limiet wordt gevonden wordt de functie afgebroken en de best gevonden uitkomst teruggegeven.

LET OP:
De gebruiker moet zelf aangeven of hij de uitkomst wil optimaliseren op basis van kosten of variantie. Dit kan middels de functies enhanced_distribution of lower_costs uit checker.py onder main. 
