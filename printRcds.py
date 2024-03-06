from connect import *

def print_records():
    try:
        cursor.execute("SELECT * FROM tblFilms")
        allRecords = cursor.fetchall()

        if allRecords:
            "INDEX 0     1     2   3    4   5"
            print("FilmID | Title                            | YearReleased | Rating | Duration(min) | Genre    ")
            print("."*100)

            for record in allRecords:
                print(f"{record[0]:6} | {record[1]:32} | {record[2]:13}| {record[3]:7}| {record[4]:14}| {record[5]:15}")
                
        else:
            print("No film found in the records")
        print("."*100)
    except sql.OperationalError as sqlOError:
        print(f"failed due to: {sqlOError}.")
    except sql.ProgrammingError as sqlPError:
        print(f"failed because of Programming Error: {sqlPError}.")
    except sql.Error as sqlError:
        print(f"failed due to: {sqlError}.")

if __name__=="__main__":
    print_records()