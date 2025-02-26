CREATE_TABLE = "CREATE TABLE IF NOT EXISTS BranchA(" \
               "'id' INTEGER," \
               "'firstName' TEXT(10) NOT NULL," \
               "'lastName' TEXT(10) NOT NULL," \
               "'phoneNumber' INTEGER(11) NOT NULL UNIQUE,"\
               "'email' TEXT(50) NOT NULL UNIQUE,"\
               "'address' TEXT(60) NOT NULL,"\
               "'salary' INTEGER(10) NOT NULL,"\
               "PRIMARY KEY('id' AUTOINCREMENT)" \
               ")"


INSERT = "INSERT INTO BranchA(id, firstName, lastName, phoneNumber, email, address, salary) VALUES(NULL,?, ?, ?, ?, ?, ?)"

FETCH_ALL = "SELECT * FROM BranchA"

SEARCH = "SELECT * FROM BranchA WHERE firstName = ? ;"

UPDATE = "UPDATE BranchA SET firstName= ?,lastName= ?,phoneNumber=?, email=?, address=?, salary=? where id = ?"

DELETE = "DELETE FROM BranchA where id = ?"
