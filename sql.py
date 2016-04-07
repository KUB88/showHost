import sqlite3

class sql(object):      
    def __init__(self):
        try:
            self.con = sqlite3.connect('C:\\Users\\yangh\\Desktop\\py\\showHost\\showHost.db')
            print('connect to db successfully')
        except Exception:
            print('failed to connect to db')
            exit(0)

    def create_table(self):
        self.con.execute('''
            CREATE TABLE HOST
           (ID INTEGER PRIMARY KEY AUTOINCREMENT     NOT NULL,
           IP             CHAR(50)    NOT NULL,
           PORT           CHAR(50),
           MAC            CHAR(50),
           SWITCHER       CHAR(50),
           BACKUP         CHAR(50),
           TIME           TimeStamp NOT NULL DEFAULT CURRENT_TIMESTAMP);
           ''')
        print('create table successfully')
        

    def _insert(self, ipadd, interfaceport, macadd, switcher, backup, table = 'HOST'):
        self.con.execute("INSERT INTO " + table + " (IP,PORT,MAC,SWITCHER,BACKUP) \
          VALUES ( ?, ?, ?, ?, ? )",(ipadd, interfaceport, macadd, switcher, backup));
        print('insert successfully')
    
    def _commit(self):
        self.con.commit()
        

    def _select(self,  method='AND',**kwargs):
        condition = []
        if len(kwargs.keys()) == 0:
            print('please give paraments')
            exit(0)
        for i in kwargs.keys():
            valus = "\'"+str(kwargs.get(i))+"\'"
            condition.append(str(i)+'='+valus)
        if method == 'AND':
            a=' AND '
        if method == 'OR':
            a=' OR '
        condition = str(a.join(condition))
        print(condition)
        res = self.con.execute("SELECT * FROM HOST WHERE "+condition)
        return res

    def _delete(self, id, table = 'HOST'):
        self.con.execute('DELETE FROM '+ table +' where ID =' + id )
        print('delete row '+id+' successfully')
        self.con.commit()
            
a=sql()
res = a._select(BACKUP='1')
for row in res:
    print(row)
#a.create_table()
    
    