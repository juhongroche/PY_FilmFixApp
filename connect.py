import sqlite3 as sql

try:
    with sql.connect("PY_FilmFixApp/filmflix.db") as con: 
        # con => database connect to the variable sql which is the link to sqlite3
        cursor=con.cursor() 
except sql.OperationalError as sqlOError:
    print(f"SQL connection failed: {sqlOError}")

    