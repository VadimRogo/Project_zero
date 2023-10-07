import os
from datetime import date, datetime

direrctory = "C:\Practice\personas"
files = os.listdir(direrctory)
date = date.today()
now = datetime.now()
nowPeople = now.strftime("%H:%M")
time = now.strftime("%H")
print(files)


def dialog(name):
    someone = ''
    me = ''
    if f'{name}.txt' in files :
        with open(f'C:\Practice\personas\{name.lower()}.txt', 'a') as f:
            f.writelines(f'\n{nowPeople}_______New dialog______{date}______  \n')
        for i in files:
            if name.lower() == i[:-4].lower():
                print("\n Let's talk \n")
                while someone != 'stop' and me != 'stop':
                    someone = input(f'{name} --- ')
                    me = input('me --- ') 
                    
                    record_dialog(name, someone, me)
    else:
        print("Sorry, persona not find")
def record_dialog(name, someone, me):
    with open(f'C:\Practice\personas\{name}.txt', 'a') as f:
        if someone != 'stop' or me != 'stop':
            f.writelines(f'{name} ---  ' + someone + '\n')
            f.writelines('Vadim ---  ' + me + '\n')

class new_persona:
    def __init__(self) -> None:
        self.name = input("Your name? \n")
        self.age = input("Your age? \n")
        self.wannaTell = input("What you wanna tell? \n")
        self.comment = input("Maybe you wanna tell something like comment? \n")
        new_persona.main_data(self)
        self.wannaTalk = input("Wanna talk or something? \n")
        if self.wannaTalk.lower() == 'yes':
            dialog(self.name)
        else:
            return 0


    def main_data(obj):
        with open(f"C:\Practice\personas\{obj.name}.txt", "w") as f:
            f.writelines("Name : " + obj.name + " " + "Age : " + obj.age + "\n")
            f.writelines("Want to tell : " + obj.wannaTell + "\n")
            f.writelines("Comment : " + obj.comment + "\n")

class old_person():
    def __init__(self) -> None:
        self.wannaTell = input("What you wanna Tell? \n")
        self.fellings = input("What you fell? \n")
        self.talk = input("Let's talk some? \n")   
        pass

option = input("Wanna talk text something or maybe \n")
if option.lower() == "talk":
    test = input("Old or new? \n")
    if test.lower() == 'new':
        persona = new_persona()
    elif test.lower() == 'old':
        name = input("What's your name? ")
        dialog(name)
elif option.lower() == 'journal':
    text = ''
    print("\n_____JOURNAL OPEN_____\n")
    with open(f"C:\Practice\journals\{date}_{time}.txt", "a") as f:
        while text != "stop":
            text = input()
            if text != "stop":
                f.writelines(text)