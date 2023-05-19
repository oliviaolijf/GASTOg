#ADT Zaal Gemaakt door: Minh Hoang

class Zaal():

    nummer = 0
    aantalPlaatsen = 0

    def __init__(self, nummer, aantalPlaatsen):
        """
        Maak een zaal.

        :param nummer: nummer van dit object
        :param aantalPlaatsen: aantal plaatsen in dit object

        preconditie: Er is geen preconditie.
        postconditie: Maakt een zaal.
        """
        self.nummer = nummer
        self.aantalPlaatsen = aantalPlaatsen

    def addZaal(self, aantalplaatsen):
        """
        Maakt nieuwe zaal aan en stopt in ketting

        preconditie: aantalplaatsen >= 0
        postconditie: er is een nieuwe zaal aangemaakt met een nummer

        :param aantalplaatsen: aantal zit plaatsen
        :return: bool of het gelukt is
        """

        print("Nieuwe zaal aangemaakt")