# ADT Reservatiesysteem Gemaakt door: groep samen
## data


## functionaliteit
class Reservatiesysteem:
    def __init__(self):
        init=True

    def maak_gebruiker(self,voornaam, achternaam, emailadres):
        """
        Maakt nieuwe gebruiker met id en zet deze in de ketting van alle gebruikers.

        :param voornaam: voornaam van gebruiker, string
        :param achternaam: achternaam van gebruiker, string
        :param emailadres: e-mailadress van gebruiker, string
        :return: id van de gebruiker

        preconditie: Er is geen preconditie.
        postconditie: Maakt een gebruiker en zet deze in de ketting van alle gebruikers.
        """
        pass

    def verwijder_gebruiker(self,id):
        """
        Verwijdert gebruiker met id.

        :param id: is een uniek getal dat overeenkomt met dit object.
        :return: True of False, als True verwijder dan gebruiker anders None.

        preconditie: Er is geen preconditie.
        postconditie: Gebruiker is verwijdert van de ketting van alle gebruikers.
        """
        pass

    def verwijder_alle_gebruikers(self):
        """
        Maakt ketting van alle gebruikers leeg.

        :return: True of False

        preconditie: Er is geen preconditie.
        postconditie: Maakt ketting van alle gebruikers leeg.
        """
        pass

    def maak_film(self,titel):
        """
        Maakt nieuwe film met id en rating 0.0 en zet deze in de ketting van alle films.

        :param titel: naam van de film, string
        :return: id van de film

        preconditie: Er is geen preconditie.
        postconditie: Maakt een film en zet deze in de ketting van alle films.
        """
        pass

    def verwijder_film(self,id):
        """
        Verwijdert film met id.

        :param id: is een uniek getal dat overeenkomt met dit object.
        :return: True of False, als True verwijder dan film anders None.

        preconditie: Er is geen preconditie.
        postconditie: Film is verwijdert van de ketting van alle film.
        """
        pass

    def verwijder_alle_films(self):
        """
        Maakt ketting van alle films leeg.

        :return: True of False

        preconditie: Er is geen preconditie.
        postconditie: Maakt ketting van alle films leeg.
        """
        pass

    def maak_zaal(self,nummer, aantal_plaatsen):
        """
        Maakt nieuwe zaal met nummer en aantal plaatsen en zet deze in de ketting van alle zalen.

        :param nummer: nummer van dit object
        :param aantal_plaatsen: aantal plaatsen in dit object
        :return: true of false

        preconditie: Er is geen preconditie.
        postconditie: Maakt een zaal en zet deze in de ketting van alle zalen.
        """
        pass

    def maak_vertoning(self,zaalnummer, slot, datum, filmid, aantal_vrije_plaatsen):
        """
        Maakt nieuwe vertoning met id en zaalnummer, slot, datum, filmid, aantal_vrije_plaatsen en zet deze in de boom van alle vertoningen.

        :param zaalnummer: nummer van zaal
        :param slot: slot van de vertoning
        :param datum: datum van de vertoning
        :param filmid: id van de film
        :param aantal_vrije_plaatsen: aantal vrije plaatsen in de vertoning
        :return: id van de vertoning

        preconditie: Er is geen preconditie.
        postconditie: Maakt een vertoning en zet deze in de boom van alle vertoningen.
        """
        pass

    def get_vertoning_met_id(self,vertoning_id):
        """
        Geeft de gevonden vertoning in de boom van alle vertoningen.

        :param vertoning_id van de vertoning

        :return: vertoning

        preconditie: Er is geen preconditie.
        postconditie: return de gevonden vertoning.
        """
        pass

    def verwijder_vertoning(self,id):
        """
        Verwijdert vertoning met id.

        :param id: is een uniek getal dat overeenkomt met dit object.
        :return: True of False, als True verwijder dan vertoning anders None.

        preconditie: Er is geen preconditie.
        postconditie: Vertoning is verwijdert van de boom van alle vertoningen.
        """
        pass

    def verwijder_alle_vertoningen(self):
        """
        Maakt ketting van alle vertoningen leeg.

        :return: True of False

        preconditie: Er is geen preconditie.
        postconditie: Maakt boom van alle vertoningen leeg.
        """
        pass

    def lijst_reservaties(self):
        """"
        Geeft de reservaties queue.

        preconditie: Er is geen preconditie.
        postconditie: Maak een reservatie voor aantal tickets van Gebruiker op bepaalde tijdstip.
        """
        pass

    def maak_reservatie(self,userid, timestamp, vertoningid, aantal_gereserveerde_plaatsen):
        """
        Maakt nieuwe reservatie met id en userid, timestamp, vertoningid, aantal_gereserveerde_plaatsten en plaatst die in de queue.

        :param userid: id van de user
        :param timestamp: tellers die beginnen op 0
        :param vertoningid: id van de vertoning
        :param aantal_gereserveerde_plaatsen: aantal plaatsen die gereserveerd worden
        :return: id van de reservatie

        preconditie: Er is geen preconditie.
        postconditie: Maak een reservatie voor aantal tickets van Gebruiker op bepaalde tijdstip.
        """
        pass

    def zoek_reservatie_met_timestamp(self,timestamp):
        """
        Zoekt reservatie met timestamp.

        :param timestamp: tellers die beginnen op 0
        :return: Lijst van reservaties met die timestamp.

        preconditie: Er is geen preconditie.
        postconditie: Geeft een lijst van reservaties met die timestamp.
        """
        pass

    def verwijder_reservatie(self,reservatie_id):
        """
        Verwijdert de reservatie uit de queue van alle reservaties met id.

        :param reservatie_id: id van de reservatie.
        :return: True of fale, als true verwijder reservatie anders None.

        preconditie: Er is geen preconditie.
        postconditie: Reservatie is verwijdert uit de queue van alle reservaties.
        """
        pass


