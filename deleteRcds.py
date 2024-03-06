from connect import *

def delete_records():
    try:
        filmID = int(input("Enter the Film ID of the record to delete: "))
        cursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {filmID}")

        row=cursor.fetchone()
        if row == None:
            print(f"No record of FILM ID '{filmID}' found, deleting the record failed.")
        else:
            cursor.execute("DELETE FROM tblFilms WHERE filmID = ?", (filmID,))
            con.commit()
            print(f"All records of {filmID} deleted from the table")

    except sql.OperationalError as sqlOError:
        print(f"failed due to: {sqlOError}.")
    except sql.ProgrammingError as sqlPError:
        print(f"failed because of Programming Error: {sqlPError}.")
    except sql.Error as sqlError:
        print(f"failed due to: {sqlError}.")

if __name__=="__main__":
    delete_records()