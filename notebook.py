from datetime import datetime
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
notes_location = str(__location__)+r"\Notes"

def start_page():
    while True:
        command = int(input("\nPodaj numer polecenia z listy:\n\n1. Dodaj nową notatkę\n2. Wyświetl wszystkie notatki\n0. Wyjdź z programu.\n--> "))
        if command == 1:
            note_name = input("Nazwa notatki: ")
            create_note(note_name)
            break
        elif command == 2:
            all_notes()
            break
        elif command == 0:
            print("Do zobaczenia!")
            break
        else:
            print("Podano nieprawidłowy numer komendy.\n")

def all_notes():
    try:
        file_list = os.listdir(notes_location)
        if len(file_list) == 0:
            print("\nBrak zapisanych notatek!\n")
            start_page()
        else:
            for file in file_list:
                with open(f"{notes_location}\{file}") as f:
                    print(f.read())
            start_page()
    except Exception as e:
        print(e.strerror)
        start_page()

def create_note(note_name):
    note_date = datetime.now().strftime(r"%Y-%m-%d~%H-%M-%S")
    note_header = datetime.now().strftime(r"%d.%m.%Y, %H:%M:%S")
    note_separator = "\n"+40*"="+"\n"
    note_txt = input("Napisz notatkę (maksymalna ilość znaków to 300):\n -->")
    if len(note_txt)>300:
      print("Notatka zawiera zbyt dużą ilość znaków!\n")
      start_page()
    else:
        try:
            with open(f"{notes_location}\{note_date}_{note_name}.txt","w",encoding="utf-8") as n:
                n.write(f"{note_separator}\n{note_header}\n\n{note_txt}\n{note_separator}\n")
                print("Notatka zapisana!")
            start_page()
        except Exception as e:
            print(e.strerror)
            start_page()

start_page()