from connect import *

def report_records():
    try:
        searchField = input("Search by FilmID or Title or YearReleased or Rating or Duration or Genre (Please enter the exact key word!): ")

        if searchField == "FilmID":
            intInput = int(input("Enter FilmID: "))
            cursor.execute("SELECT * FROM tblFilms WHERE filmID = ?",(intInput,))
            data=cursor.fetchone()
        
            if data==None:
                print(f"No record of film with ID '{intInput}' found.")
            else:
                print(data)
        
        elif searchField in ["Title", "YearReleased", "Rating", "Duration", "Genre"]:
            strInput = (input(f"Enter the data for the search field '{searchField}': "))
            cursor.execute(f"SELECT * FROM tblFilms WHERE {searchField} LIKE '%{strInput}%'")

            datas = cursor.fetchall()

            if not datas:
                print(f"No record of film matching '{searchField}': '{strInput}'")
            else:
                for record in datas:
                    print(record)
        else:
            print(f"Search field '{searchField}' invalid!\nPlease enter the right keyword from..\nFilmID or Title or YearReleased or Rating or Duration or Genre")


    except sql.OperationalError as sqlOError:
        print(f"failed due to: '{sqlOError}'.")
    except sql.ProgrammingError as sqlPError:
        print(f"failed because of Programming Error: '{sqlPError}'.")
    except sql.Error as sqlError:
        print(f"failed due to: '{sqlError}'.")

if __name__=="__main__":
    report_records()
