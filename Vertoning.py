#ADT Vertoning gemaakt door: Olivia Wuyts
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None

def createTreeItem(key, value):
    return Node(key, value)

class BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def searchTreeInsert(self, item):
        if self.isEmpty():
            self.root = item
            return True
        else:
            current = self.root
            found = False
            while found is False:
                if current.key > item.key:
                    if current.leftChild is None:
                        current.leftChild = item
                        return True
                    else:
                        current = current.leftChild

                elif current.key < item.key:
                    if current.rightChild is None:
                        current.rightChild = item
                        return True
                    else:
                        current = current.rightChild

    def print(self):
        pass

    def searchTreeDelete(self, key):
        if self.searchTreeFind(key) == False:
            print("This item does not exist in the tree")
            return False
        parent = None
        current = self.root
        while current.key != key:
            if current.key < key:
                parent = current
                current = current.rightChild
            elif current.key > key:
                parent = current
                current = current.leftChild
        if current.leftChild == None and current.rightChild == None:
            current = None
            return True

        elif current.leftChild == None:
            temp = current.rightChild
            current.rightChild = None
            current = temp
            return True

        elif current.rightChild == None:
            temp = current.leftChild
            current.leftChild = None
            currnet = temp
            return True

        else:
            smallesRightElement = None
            smallesRightElement = current.rightChild
            while smallesRightElement.leftChild != None:
                smallesRightElement = current.leftChild

            current = smallesRightElement
            smallesRightElement = None
            return True


    def searchTreeFind(self, key):
        current = self.root
        found = False
        end = False
        if self.root == None:
            return False
        while found is False and end is False :
            if current.key < key:
                if current.rightChild is not None:
                    current = current.rightChild
                else:
                    end = True
            elif current.key > key:
                if current.leftChild is not None:
                    current = current.leftChild
                else:
                    end = True
            elif current.key == key:
                found = True
        if found:
            return True

    def clearTree(self):
        while self.root.leftChild != None:
            current = self.root
            parent = None
            while current.leftChild != None:
                parent = current
                current = current.leftChild
            if current.leftChild is None:
                parent.leftChild = None

        while self.root.rightChild != None:
            current = self.root
            parent = None
            while current.rightChild != None:
                parent = current
                current = current.rightChild
            if current.rightChild is None:
                parent.rightChild = None
        self.root = None
        return True



class Vertoning():

    id = 0
    zaalnummer = 0
    slot = 0
    datum = 0
    filmid = 0
    aantalPlaatsen = 0

    def __init__(self, id, zaalnummer, slot, datum, filmid, aantalPlaatsen):
        """
        Initialise een vertoning op het slot voor de film in de zaal.

        :param id: is een uniek getal dat overeenkomt met dit object
        :param zaalnummer: nummer van zaal
        :param slot: slot van de vertoning
        :param datum: datum van de vertoning
        :param filmid: id van de film
        :param aantalPlaatsen: aantal vrije plaatsen in de vertoning

        preconditie: Er is geen preconditie.
        postconditie: Maak een vertoning op het slot voor de film in de zaal.
        """
        self.id = id
        self.zaalnummer = zaalnummer
        self.slot = slot
        self.datum = datum
        self.filmid = filmid
        self.aantalPlaatsen = aantalPlaatsen

        self.originelePlaatsen = aantalPlaatsen
        self.bezig = False

    def makeNode(self):
        return Node(self.id, self)

    def subtractSeats(self, reservatie, vertoning):
        """
        verlaagt het aantal zit plaatsen met hoeveel mensen er gereserveerd hebben in het reservatie object

        preconditie: aantal zitplaatsen vertoning - gereserveerde plaatsen >= 0
        postconditie: aantal zitplaatsen is verminderd en >= 0

        :param reservatie: reservatie object
        param vertoning: gegeven vertoning
        :return: bool of het gelukt is
        """
        if vertoning.aantalPlaatsen >= reservatie.gereserveerd:
            vertoning.aantalPlaatsen -= reservatie.gereserveerd
            print("Aantal zitplaatsen verminderd")
            return True
        else:
            print("Er zijn niet genoeg vrije zitplaatsen om deze reservatie door te voeren.")
            return False

    def startVertoning(vertoning, datum, tijd):
        """
        start de vertoning van een gegeven film

        preconditie: er is een vertoning
        postconditie: de vertoning is gestart

        :param vertoning: vertoning
        :return: bool of het gelukt is
        """
        if vertoning.bezig is False and vertoning.datum == datum and vertoning.slot == tijd:
            vertoning.bezig = True
            print("Start vertoning")
            return True
        else:
            print("Deze vertoning kan momenteel niet gestart worden")
            return False

    def endVertoning(vertoning):
        """
        stopt de vertoning en zet zitplaatsen weer vrij

        preconditie: er is een vertoning
        postconditie: de vertoning is beëindigd

        :param vertoning: vertoning
        :return: bool of het gelukt is
        """

        if vertoning.bezig is True:
            vertoning.bezig = False
            vertoning.aantalPlaatsen = vertoning.originelePlaatsen
            print("Einde vertoning")
            return True
        else:
            print("Deze vertoning is nog niet gestart en kan dus niet beëindigd worden.")
            return False



class Vertoningen():
    boomVertoningen = None

    def __init__(self):
        self.boomVertoningen = BST()

    def addvertoning(self, vertoning):
        """
        maak een nieuwe vertoning aan en plaats die in de boom van alle vertoningen

        precondities: alle parameters zijn >=0
        postcondities: er is een nieuwe vertoning aangemaakt, met een id en filmid (zelfde concept zoals de rest id = id + 1).

        :param vertoning: vertoning object dat zal toegevoegd worden
        :return: bool of het gelukt is
        """
        if self.boomVertoningen.searchTreeFind(vertoning.id):
            print("Er bestaat al een vertoning met deze id")
            return False
        self.boomVertoningen.searchTreeInsert(vertoning.makeNode())
        print("Vertoning aangemaakt")
        return True

    def removeAllVertoningen(self):
        """
        verwijdert alle vertoningen

        preconditie: er is een vertoning
        postconditie: alle vertoningen zijn verwijderd

        :return: bool of het gelukt is
        """
        if self.boomVertoningen.root is None:
            print("Boom met vertoningen is al leeg er kan niets verwijderd worden")
            return False
        self.boomVertoningen.clearTree()
        print("Alle vertoningen verwijderd")
        return True


if __name__ == '__main__':
    pass