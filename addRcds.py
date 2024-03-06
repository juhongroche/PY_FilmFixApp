from connect import *

def add_records():
    try:
        print("Enter record below.")
        title = input("Title: ")
        year = input("Release year: ")
        rating = input("Rating: ")
        duration = input("Duration(minutes): ")
        genre = input("Genre: ")

        cursor.execute("INSERT INTO tblFilms VALUES(NULL,?,?,?,?,?)", (title,year,rating,duration,genre))

        con.commit()
        print(f"{title} added into the tbleFilms table")
    
    except sql.OperationalError as sqlOError:
        print(f"failed due to: {sqlOError}.")
    except sql.ProgrammingError as sqlPError:
        print(f"failed because of Programming Error: {sqlPError}.")
    except sql.Error as sqlError:
        print(f"failed due to: {sqlError}.")

if __name__=="__main__":
    add_records()