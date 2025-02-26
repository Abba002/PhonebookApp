CREATE_TABLE = "CREATE TABLE IF NOT EXISTS BranchB(" \
               "'id' INTEGER," \
               "'firstName' TEXT(10) NOT NULL," \
               "'lastName' TEXT(10) NOT NULL," \
               "'phoneNumber' INTEGER(10) NOT NULL UNIQUE,"\
               "'email' TEXT(50) NOT NULL UNIQUE,"\
               "'address' TEXT(60) NOT NULL,"\
               "'salary' INTEGER(10) NOT NULL,"\
               "PRIMARY KEY('id' AUTOINCREMENT)" \
               ")"


INSERT = "INSERT INTO BranchB(id, firstName, lastName, phoneNumber, email, address, salary) VALUES(NULL,?, ?, ?, ?, ?, ?)"

FETCH_ALL = "SELECT * FROM BranchB"

UPDATE = "UPDATE BranchB SET firstName= ?,lastName= ?,phoneNumber=?, email=?, address=?, salary=? where id = ?"

DELETE = "DELETE FROM BranchB where id = ?"
