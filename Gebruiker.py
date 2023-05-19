# ADT Gebruiker gemaakt door: Sinem Erdön

class Gebruiker():

    id = 0
    voornaam = ""
    achternaam = ""
    email = ""

    def __init__(self,id,voornaam,achternaam,email):
        self.id = id
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.email = email

    def addGebruiker(self, voornaam, achternaam, email):
        """
        Maakt een nieuwe gebruiker aan en plaats die in de ketting van alle gebruikers, id wordt niet meegegeven
        maar de id wordt +1 gedaan (zelfde concept zoals addFilm).

        preconditie: naam en email zijn strings (merk op email moet ook een bepaalde structuur volgen)
        postconditie: er wordt een nieuwe gebruiker aangemaakt.

        :param voornaam: voornaam van de gebruiker
        :param achternaam: achternaam van de gebruiker
        :param email: email van de gebruiker
        :return: bool of het gelukt is
        """

        print("gebruiker 'addGebruiker' is toegevoegd aan de kettingt")

    def removeGebruikers(self):
        """
        Verwijder alle gebruikers van de ketting

        preconditie: er moet minstens 1 gebruiker zijn
        postconditie: alle gebruikers zijn van de ketting verwijdert, de ketting is leeg

        :return: bool of het gelukt is
        """
        print("Alle gebruikers zijn verwijderdt van de ketting")