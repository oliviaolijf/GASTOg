#ADT Reservatie gemaakt door: groep samen

class reservatie():

    id = 0
    userid = 0
    timestamp = 0
    vertoningid = 0
    gereserveerd = 0

    def __init__(self,id, userid, timestamp, vertoningid, gereserveerd):
        """
        Initialise een reservatie voor aantal tickets van Gebruiker op bepaalde tijdstip.

        :param id: is een uniek getal dat overeenkomt met dit object
        :param userid: id van de user
        :param timestamp: tellers die beginnen op 0
        :param vertoningid: id van de vertoning
        :param gereserveerd: aantal plaatsen die gereserveerd worden

        preconditie: Er is geen preconditie.
        postconditie: Maak een reservatie voor aantal tickets van Gebruiker op bepaalde tijdstip.
        """
        self.id = id
        self.userid = userid
        self.timestamp = timestamp
        self.vertoningid = vertoningid
        self.gereserveerd = gereserveerd

    def addReservatie(self, id, userid, timestamp, gereserveerd):
        """
        Maakt een reservatie voor een aantal mensen en krijgt een vertoningsid mee terug

        preconditie: alle parameters moeten >= 0 zijn/
        postconditie: er is een reservatie aangemaakt en ze krijgen hun vertoningsid.

        :param id: reservatie id
        :param userid: klant id
        :param timestamp: tijdslot en datum
        :param gereserveerd: aantal mensen gereserveerd
        :return: bool of het gelukt is
        """
        print("Nieuwe reservatie aangemaakt")

    def push(self, reservatie):
        """
        Achteraan in de queue wordt een reservatie begevoegt

        preconditie: reservatie mag niet None zijn
        postconditie: de reservatie is gepushed in de queue

        :param reservatie: reservatie object
        :return: bool of het gelukt is
        """
        print("Reservatie erbij")

    def getQueue(self):
        """
        Krijgt de reservatie systeem oftwel de queue

        preconditie: queue mag niet leeg zijn
        postconditie: eerst volgende reservatie wordt afgedrukt

        :return: reservatie
        """
        print("De eerste volgende reservatie is:")

    def pop(self):
        """
        verwijdert de eerste reservatie van de queue

        preconditie: queue mag niet leeg zijn
        postconditie: eerste reservatie wordt verwijderdt

        :return: reservatie
        """

        print("De verwijderde element is:")