import sqlite3

        
def connect_db():
    try:
        con = sqlite3.connect('C:\\Users\\yangh\\Desktop\\py\\showHost\\showHost.db')
        print('connect to db successfully')
        return con
    except Exception:
        print('failed to connect to db')
        exit(0)

def create_table():
    con = connect_db()
    con.execute('''
        CREATE TABLE HOST
       (ID INTEGER PRIMARY KEY AUTOINCREMENT     NOT NULL,
       IP             CHAR(50)    NOT NULL,
       PORT           CHAR(50)     NOT NULL,
       MAC            CHAR(50)     NOT NULL);
       ''')
    print('create table successfully')
    con.close()

def _insert(ipadd, interfaceport, macadd, table = 'HOST'):
    con = connect_db()
    con.execute("INSERT INTO " + table + " (IP,PORT,MAC) \
      VALUES ( ?, ?, ? )",(ipadd, interfaceport, macadd));
    con.commit()
    print('insert successfully')
    con.close()

def _select():
    con = connect_db()
    res = con.execute("SELECT * FROM HOST")
    for row in res:
        print(row)

def _delete(id, table = 'HOST'):
    con = connect_db()
    con.execute('DELETE FROM '+ table +' where ID =' + id )
    print('delete row '+id+' successfully')
    con.commit()
    con.close    

#create_table()
#_insert('1.1.1.1', 'gi1/1', '6666-6666-6666')
#_delete('11')
#_select()
    
    