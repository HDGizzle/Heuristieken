# Heuristieken --> Radio Russia

Deze repository is in drie verschillende mappen onderverdeeld:

1) initialiser
2) algorithms
3) main

De initialiser map bevat csv data en de functies om de algoritmes te initialiseren. De provincies en buren worden vanuit de csv's naar de initialiser geladen, welke vervolgens wordt gebruikt in de algoritmes.

De algorithms map bevat 4 verschillende algoritmes. 3 algoritmes zijn bestemd voor het oplossen van de opdracht. Het vierde algoritme is ontworpen om de statespace van de opdracht uit te rekenen. 

De main map bevat een stuk code dat alle data en algoritmes centraliseert, waardoor men vanuit 1 centrale plek het gewenste algoritme voor het gewenste land kan uitvoeren. 

Pijnpunten opdracht:

Hoge complexiteit van het probleem:
    Het aanpassen van een provincie heeft een effect op alle nabijgelegen buren en de buren van de buren eromheen.
    Dit maakt met name het toepassen van een hillclimber onvoorspelbaar en soms weinig nuttig

Verschillende doelen die niet per se met elkaar verenigbaar zijn:
    Het vinden van de zenderverdeling met de laagste variantie en zendergebruik komt niet overeen met het vinden van
    een goedkoopste oplossing, vanwege het grote kostenvoordeel bij de eerste zendertypes. Hierdoor is het 
    voordelig om zoveel mogelijk van deze zendertypes te plaatsen wat uiteindelijk tot een scheve verdeling kan
    leiden. Dit zorgt ervoor dat functies om de zendervariantie te minimaliseren niet toepasbaar zijn voor het 
    kostenprobleem

Objective functions onvoorspelbaar:
    Aanvankelijk dachten we dat het vinden van clusters een belangrijke graadmeter was om de minimale hoeveelheid zenders
    te bepalen. Echter is de gemiddelde hoeveelheid buren ook van belang, zoals in het geval kan Nederland
    (ons testvoorbeeld) blijkt. Hier is de maximale grootte van een cluster 3 provincies, maar tot nu toe is het
    niet mogelijk deze met 3 zenders in te vullen. 

Grootte van het probleem:
    Al bij een gebied van 20 provincies (kleiner dan de minimale hoeveelheid provincies die in de case moeten worden 
    behandeld) is het niet meer mogelijk om binnen afzienbare tijd de totale hoeveelheid oplossing te vinden. 
    Hierdoor is het met name bij de kostenfunctie lastig te bepalen of daadwerkelijk een efficiënte oplossing is
    gevonden, behalve door zoveel mogelijk oplossingen met elkaar te vergelijken.

Visualistie: 
    Vinden van geschikte shapefiles voor landen met obscure spelling (Oekraïne en Rusland) en de namen van onze
    provincies met onze in de shapefile te vergelijken.
