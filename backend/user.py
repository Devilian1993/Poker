# import UI

class User:

    taken_usernames = set()   # przechowuje zajete nazwy uzytkownikow

    def __init__(self, username, balance, email, password, phone_number):
        self.username = username
        self.phone_number = phone_number
        self.balance = balance
        self.email = email
        self.password = password

    @classmethod
    def load_taken_usernames(cls):     # wczytywanie taken_usernames z 'data.txt'
        with open("data.txt", "r") as file:
            for line in file:
                parts = line.strip().split(', ')    # parts = username (jak zajrzysz na 'data.txt' to zczytuje pierwszy fragment linijki
                if len(parts) > 0:
                    cls.taken_usernames.add(parts[0])   # Dodaje do set'u 'taken_usernames'

    @classmethod
    def if_available_username(cls, username):
        if username in cls.taken_usernames:
            return False
        return True   # wiadomo. jak w nazwie. sprawdza czy nazwa jest dostepna (jak dostepna to zwraca True)


    @classmethod
    def main(cls):   # Główna metoda, która sie uruchamia za kazdym razem
        while True:
            print("Available actions : \n1. Login\n2. Register\n3. Forgot Password (doesn't work obv)")
            decision = input("What would you like to do? :  ")
            print('\n')
            if decision == "1":
                cls.login()
                break
            elif decision == "2":
                cls.register()
                break
            elif decision == "3":
                print("Currently, it doesn't work ;( \n")

    @classmethod
    def login(cls):
        cls.load_taken_usernames()  # wczytuje zajete nazwy uzytkownika
        # logowanie
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            user_found = False   # przełącznik, czy znaleziono uzytkowniak

            with open("data.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(', ')
                    if len(parts) > 1 and parts[0] == username:
                        user_found = True
                        if parts[1] == password:
                            print("Login successful")
                            return   # Tu zrobie potem zeby po zalogowaniu pokazywalo dostepne opcje
                        else:
                            print("Invalid password. Please try again.")
                            break   # break dla for'a. While podtrzymany dopoki nie wprowadzi sie poprawnego hasla.

            if not user_found:   # if user_found == False (jak nie znaleziono)
                print("Invalid username. Please try again.")


    @classmethod
    def register(cls):   # metoda pozwalajca na rejestracja (z reszta wiadomo -- Register)
        cls.load_taken_usernames()  # ładuje zajete usernames

        while True:
            username = input("Enter your username: ")
            if cls.if_available_username(username) == False:   # JEZELI ZAJETE
                print("Sorry, that username is already taken.")
            else:
                break   #JEŻELI NIE ZAJETE TO WYCHODZI Z WHILE I PYTA O PASSWORD

        while True:
            password = input("Enter your password: ")
            confirm_password = input("Confirm your password: ")
            if password != confirm_password:
                print("Sorry, your passwords don't match. Try again.")  # gdy hasla sie nie zgadza
            else:
                break    # JEZELI WSZYSTKO SIE ZGADZA WYCHODZI Z WHILE. Nastepnie wypytuje o reszte informacji (nr tel, mail)

        while True:
            phone_number = input("Enter your phone number: ")
            if phone_number.isdigit() == False:
                print("Sorry, your phone number must contain just digits.") # error gdy blad w numerze
            else:
                break   # JEZELI WSZYSTKO SIE ZGADZA WYCHODZI Z WHILE. Potem pyta o mail'a.

        while True:
            email = input("Enter your email: ")
            if '@' not in email: #brak '@' error
                print("Sorry, you must enter a valid email address.") # error gdy blad w mail'u
            else:
                break  # gdy wszystko sie zgadza tworzy konto. Registeration succesful

        new_user = cls(username=username, balance=500, email=email, password=password, phone_number=phone_number)
        #default balance to 500$. Tworzy nowego uzytkownika ktory ma wlasne dane

        with open("data.txt", "a") as file:
            file.write(f"{username}, {password}, {email}, {phone_number}, {new_user.balance}\n")
            # zapisuje do pliku w powyzszym formacie
            # username, haslo, mail, numer telefonu, defaultowy balans (500)

        print("Registration succesful") # komunikat #


