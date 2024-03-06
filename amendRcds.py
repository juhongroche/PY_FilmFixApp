from connect import *

def amend_records():
    try:
        filmID = int(input("Enter the Film ID of the record to amend: "))
        cursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {filmID}")
        record=cursor.fetchone
        if record == None:
            print(f"No record of FILM ID '{filmID}' found, updating the record failed.")
        else:
            print("Enter data below.")
            title = input("Title: ")
            year = input("Release year: ")
            rating = input("Rating: ")
            duration = input("Duration(minutes): ")
            genre = input("Genre: ")

            cursor.execute(f"UPDATE tblFilms SET title = ?, yearReleased = ?, rating =?, duration = ?, genre =? WHERE filmID = ?", (title,year,rating,duration,genre,filmID))
            con.commit()
            print(f"'{title}' with ID '{filmID}' record amended.")


    except sql.OperationalError as sqlOError:
        print(f"failed due to: {sqlOError}.")
    except sql.ProgrammingError as sqlPError:
        print(f"failed because of Programming Error: {sqlPError}.")
    except sql.Error as sqlError:
        print(f"failed due to: {sqlError}.")

if __name__=="__main__":
    amend_records()