Depth First Algorithm
=====================

Het algoritme doorzoekt systematisch alle oplossingen binnen de state space en gaat daarbij stap voor stap alle provincies af. Provincies worden gezien als nodes in een niet vantevoren vastgesteld pad. Het pad wordt bijgehouden door middel van een stack en een visited set. Als de stack leeg is, is er sprake van een uitkomst, aangezien dan alle provincies zijn bezocht. 

LET OP:
De gebruiker heeft keuze uit twee heuristieke functies voor het kiezen van een zender:
1) low_variance_picker
of 
2) low_cost_picker

De eerste functie zorgt voor een gelijke verdeling in het gebruik van zenders en de tweede zorgt ervoor dat goedkope zenders voorrang krijgen in het plaatsen van zenders. 

Daarnaast kunnen de uitkomsten vergeleken worden met de functies enhanced_distribution of lower_costs uit checker.py
