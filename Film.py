#ADT Film gemaakt door: Michael Livchits
import io

class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class LinkedChain():
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def getLength(self):
        return self.size

    def retrieve(self,index):
        if self.head == None:
            return [0,False]
        elif index > self.size:
            return [0,False]
        else:
            toLoop = self.head
            for i in range(1,index+1):
                if i == index:
                    return [toLoop.item,True]
                toLoop = toLoop.next
        return [0,False]


    def insert(self,index,value):
        current = Node(value)
        toLoop = self.head
        if index > self.size+1:
            return False
        elif self.head == None:
            self.head = current
            self.head.next = current
            self.head.prev = current
            self.size += 1
            return True
        elif index == 1:
            current.next = self.head
            current.prev = self.head.prev
            self.head.prev.next = current
            self.head.prev = current
            self.head = current
            self.size += 1
            return True
        else:
            for i in range(1,index+1):
                if i == index-1:
                    if index == self.size+1:
                        toLoop.next = current
                        current.prev = toLoop
                        current.next = self.head
                        self.head.prev = current
                        current.item = value
                        self.size += 1
                        return True
                    else:
                        current.prev = toLoop
                        current.next = toLoop.next
                        current.next.prev = current
                        toLoop.next = current
                        current.item = value
                        self.size += 1
                        return True
                toLoop = toLoop.next



    def save(self):
        list = []
        current = self.head
        for i in range(self.size):
            list.append(current.item)
            current = current.next
        return list

    def load(self,list):
        self.head = Node
        self.head.item = list[0]
        self.size = len(list)
        current = self.head
        for i in range(1,len(list)):
            new = Node(list[i])
            current.next = new
            new.prev = current
            if i == len(list)-1:
                new.next = self.head
                self.head.prev = new
            current = current.next


    def delete(self,index):
        if self.head == None or index > self.size+1 or 0 > index-1:
            return False
        elif self.size == 1:
            self.head = None
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            if index == 1:
                self.head = current.next
        self.size -= 1
        return True

class Film():
    id = 0
    titel = ""
    rating = 0.0

    def __init__(self,id,titel,rating):
        self.id = id
        self.titel = titel
        self.rating = rating


    def addFilm(self):
        titles = []
        openFile = "data\\system.txt"

        with open(openFile, 'r') as file:
            # alle regels worden lijn per lijn afgegaan
            content = file.readlines()
            # loop door alle regels 1 per 1
            for i in content:
                ifEmpty = False
                if i == "\n":
                    ifEmpty = True
                linePerLine = i

                if ifEmpty == False:
                    # splits alle delen en verwijder de ""
                    parts = linePerLine.split('"')

                    # als de lijn start met film spring dan in de if statement
                    if parts[0].split()[0] == "film":
                        # verwijder de film gedeelte van de it
                        parts[0] = parts[0].split()[-1]

                        # stel alle gesplitste delen op met de overeenkomstige stukken

                        id = int(parts[0])
                        title = parts[1]
                        rating = parts[2].strip()

                        titles.append(title)

                        samen = [id, title, rating]

                        # print het resultaat
                        print(titles)
                        print("Film", title, "is toegevoegd aan de ketting")
        return titles

        """
        Maak een nieuwe film met een bepaalde titelen een rating die wordt meegegeven

        preconditie: id, titel en rating worden meegegeven.
        postconditie: er is een nieuwe film aangemaakt en wordt gestopt in de ketting.

        :param titel: film titel
        :param rating: film rating
        :return: bool of het gelukt is
        """

    def removeFilm(self, film):
        """
        verwijdert film

        preconditie: er is een film object
        postconditie: de gegeven film wordt verwijderd

        :param film: film object
        :return: bool of het gelukt is
        """
        print("Film 'addFilm' is toegevoegd aan de ketting")

    def removeAll(self):
        """
        Verwijdert alle films in de ketting.

        preconditie: er moet tenminste 1 film zijn.
        postconditie: alle films worden

        :return: bool of het gelukt is
        """
        print("Alle filmen zijn verwijderdt van de ketting")

l = LinkedChain()
list = Film.addFilm(0)
for i in range(len(list)):
    l.insert(i,list[i])
print(l.save())