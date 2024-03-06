import addRcds, amendRcds, printRcds, deleteRcds, report_Menu


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

        option = input("Enter the number of option from the list above: ")

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
            printRcds.print_records()
        case _:
            mainApp = False
input("Press enter to exit the app.")
        

