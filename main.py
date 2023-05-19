# global time variable
time = 0


def vervangTijd(tijd, newTijd):
    """
    zet de tijd op newTijd

    preconditie: time en newTijd > 0
    postconditie: time = newTijd

    :param tijd: oude tijd
    :param newTijd: nieuwe tijd
    :return: bool of het gelukt is
    """
    tijd = newTijd
    print("time vervangen")

def verhoogTijd(tijd):
    """
    Verhoog global variabele met 1

    preconditie: tijd >= 0
    postconditie: tijd++

    :param tijd: de tijd
    :return: bool of het gelukt is
    """
    tijd += 1
    print("tijd verhoogd")

