import addRcds, amendRcds, printRcds, deleteRcds
from connect import *

def read_file(file_path):
    try:
        with open(file_path) as readFile:
            rF=readFile.read()
            return rF
    except FileNotFoundError as notFoundError:
        print(f"File not found due to '{notFoundError}'")

def options_menu():
    option = 0
    options =["1","2","3","4","5"]
    optionList = read_file("PY_FilmFixApp/appMenu.txt")

    while option not in options:
        print(optionList)

        option = input("Enter the option from the menu above: ")

        if option not in options:
            print(f"Invalid option: '{option}' is not in the list!")
    return option


mainApp = True
while mainApp:
    mainMenu = options_menu()

    match mainMenu:
        case "1":
            addRcds.add_records()
        case "2":
            deleteRcds.delete_records()
        case "3":
            amendRcds.amend_records()
        case "4":
            def report_menu():
                option = 0
                options =["1","2","3","4","5"]
                optionList = read_file("PY_FilmFixApp/reportMenu.txt")

                while option not in options:
                    print(optionList)

                    option = input("Enter the report option from the list above: ")

                    if option not in options:
                        print(f"\nInvalid option: '{option}' is not in the list!\nEnter a valid option from the list below:\n")
                return option

            mainProgram = True
            while mainProgram:
                mainMenu = report_menu()

                if mainMenu == "1":
                    printRcds.print_records()
                elif mainMenu == "2":
                    inputField2 = input("Enter the genre:  ")
                    cursor.execute(f"SELECT * FROM tblFilms WHERE genre LIKE '%{inputField2}%'")
                    data2 = cursor.fetchall()
                    if not data2:
                        print(f"No record of '{inputField2}' found. Try others!\n")
                    else:
                        for record2 in data2:
                            print(record2)
                elif mainMenu == "3":
                    inputField3 = input("Enter the year of release:  ")
                    cursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased LIKE '%{inputField3}%'")
                    data3 = cursor.fetchall()
                    if not data2:
                        print(f"No record of '{inputField3}' found. Try others!\n")
                    else:
                        for record3 in data3:
                            print(record3)
                elif mainMenu == "4":
                    inputField4 = input("Enter the rating:  ")
                    cursor.execute(f"SELECT * FROM tblFilms WHERE rating LIKE '%{inputField4}%'")
                    data4 = cursor.fetchall()
                    if not data4:
                        print(f"No record of '{inputField4}' found. Try others!\n")
                    else:
                        for record4 in data4:
                            print(record4)
                else:
                    mainProgram = False
            input("\nPress ENTER to return to the previous menu.")
        case _:
            mainApp = False
input("Press ENTER to exit the app.")
        

