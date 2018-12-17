Main
=====

## checker.py
Checker.py bevat algemene hulpfuncties voor het uitvoeren van andere algoritmes. De hulpfuncties kunnen als volgt worden geclassificeerd:

1) Functies om uitkomsten mee op te slaan
2) Functies om zenders te plaatsen of verwijderen
3) Functies om varianties en kosten van uitkomsten uit te rekenen
4) Functies om uitkomsten met elkaar te vergelijken gebaseerd op kosten op zenderfrequentie

## main.py
Main.py wordt gebruikt om alle functies aan te roepen voor de vier verschillende landen. In de main file wordt gespecifieerd welke csv file gebruikt moet worden, waarbij de gebruiker keuze heeft uit vier verschillende bestanden:

ukraine_borders.csv
russia_borders.csv
china_borders.csv
usa_borders.csv

Als eerste stap wordt de informatie uit de csv bestanden opgehaald om de provincie objecten mee te initialiseren en te bewaren in een dictionary, waarbij de de naam van de provincie wordt gebruikt als key voor de betreffende provincie. Daarna worden de provincies meegegeven aan de drie verschillende algoritmen: depthfirst, Wellsh Powell (greedy) en hillclimber. De functies kunnen met elkaar worden vergeleken door middel van de plots die zijn opgeslagen in de results map.

## objects
De objects map bevat de py bestanden waarmee de klassen zenders en provincies mee kunnen worden aangeroepen. De map bevat een beschrijving van de eigenschappen van deze klassen.
