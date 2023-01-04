from api_nlp import API

class NLPApp:

    def __init__(self):
        self.__apio = API()
        self.__database = {}
        self.__first_menu()


    def __first_menu(self):

        choice = input("""
        Hello, How would like to proceed?

        1. Not a member? Register
        2. Already a member? Login
        3. Exit
        """)

        if choice == "1":
            self.__register()
        elif choice == "2":
            self.__login()
        else:
            exit()

    def __second_menu(self):

        choice = input("""
        Hello, How would like to proceed?

        1. Sentiment Analysis
        2. Emotion Analysis
        3. Abuse Analysis
        4. Logout
        """)

        if choice == "1":
            self.__sentiment()
        elif choice == "2":
            self.__emotion()
        elif choice == "3":
            self.__abuse()
        else:
            self.__logout()

    
    def __login(self):
        print("\n")
        print("********** Login **********")
        email = input("Enter Email:")
        password = input("Enter Password:")

        if email in self.__database:
            if password == self.__database[email][1]:
                print("Login Successful")
                self.__second_menu()
            else:
                print("Password incorrect. Try again")
                self.__login()
        else:
            print("This email is not registered")
            self.__first_menu()
    
    def __register(self):
        print("\n")
        print("********** Register **********")
        name = input("Enter Name:")
        email = input("Enter Email:")
        password = input("Enter Password:")
        cn_password = input("Confirm Password:")

        if password != cn_password:
            print("Password does not match.")
            self.__register()

        if email in self.__database:
            print("Email already exists")
        else:
            self.__database[email] = [name,password]
            print("Registration successfull. Now login")
            self.__login()

    def __sentiment(self):
        print("\n")
        print("********** Sentiment Analysis **********")
        text = input("Enter paragraph:")
        result = self.__apio.sentiment_analysis(text)
        print(result)
        self.__second_menu()


    def __emotion(self):
        print("\n")
        print("********** Emotion Analysis **********")
        text = input("Enter paragraph:")
        result = self.__apio.emotion_analysis(text)
        print(result)
        self.__second_menu()

    def __abuse(self):
        print("\n")
        print("********** Abuse Analysis **********")
        text = input("Enter paragraph:")
        result = self.__apio.abuse_analysis(text)
        print(result)
        self.__second_menu()


    def __logout(self):
        print("\n")
        print("Logged out Successfully")
        self.__first_menu()

obj = NLPApp()

