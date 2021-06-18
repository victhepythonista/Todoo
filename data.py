# database manager
import sqlite3, pandas,os
from datetime import  datetime

DATABASE = './data/APPDATA.db'

CREATE_PENDING_TABLE = """
CREATE TABLE PENDING (
    ID INT PRIMARY KEY NOT NULL,
    DESCRIPTION     TEXT    NOT NULL,
    PRIORITY        TEXT    NOT NULL,
    STATE       INT     NOT NULL);
    """

CREATE_DONE_TABLE = """
CREATE  TABLE   DONE(
     ID INT PRIMARY KEY  NOT NULL,
     DESCRIPTION    TEXT    NOT NULL,
     DATECOMPLETED  TEXT        NOT NULL
);"""
class DATAMANAGER:
    def __init__(self):
        self.conn = None


    def open_db(self):
        # open and make sure the database is working ok
        self.conn = sqlite3.connect(DATABASE)

    def close_db(self):
        self.conn.commit()
        self.conn.close()
    def allocate_index(self, table):
        cursor = self.conn.execute(f"""
        SELECT COUNT(*) from {table}""")
        RES = cursor.fetchone()
        number = RES[0]
        return(number + 1)
    def reset_database(self):
        # create two tales for pending and DONE
        os.remove(DATABASE)
        self.open_db()
        self.conn.execute(CREATE_PENDING_TABLE)
        self.conn.execute(CREATE_DONE_TABLE)
        self.conn.commit()
        self.conn.close()
        print("[-] resetting database !!")

    def add_pending(self,description, priority = 'high', state = 0 ):
        self.open_db()
        index = self.allocate_index('PENDING')
        values =  f'''{description},{priority},{state}'''
        command = f'''INSERT INTO PENDING(ID,DESCRIPTION, PRIORITY,STATE)
                    VALUES({index}, '{description}', '{priority}', '{state}');'''

        print(self.conn.execute(command))
        self.close_db()
    def remove_pending(self, ID):
        # remove a pending item with the ID provided
        self.open_db()
        command = f'''
        DELETE from PENDING where ID = {ID};
        '''
        print(command)
        self.conn.execute(command)

        self.close_db()
    def check_for_finished_items(self):
        print('CHECKING FOR COMPLETED ......')
        self.open_db()
        items_to_remove = []

        cursor = self.conn.execute('''
        SELECT id,description,state from PENDING''')
        for row in cursor:
            if row[2] == 1 :
                items_to_remove.append([row[0], row[1]])
        print('FOUND  {', len(items_to_remove), '}  COMPLETED ITEMS .....')
        self.close_db()
        # remove finished items with the state 1
        #datetie.datetime.now().strftime("%d%Y%H%M%m")
        now = datetime.now().strftime("%H:%M  %d-%m-%Y")
        # add finished items to DONE TABLE
        for itm in items_to_remove:
            print('new done item', itm)
            self.add_done(itm[0], itm[1])
        # close and commit


        for itm in items_to_remove:
            self.remove_pending(itm[0])



    def update_state(self, id):
        print('updating ', id)
        self.open_db()

        command = f'''
        UPDATE PENDING set STATE = 1 where ID = '{id}' ;'''
        self.conn.execute(command)
        self.close_db()
        self.check_for_finished_items()
    def read_pending(self):
        # retuen a list of all pending items
        self.open_db()
        CURSOR = self.conn.execute('''
        SELECT id, description, state from PENDING''')
        data = []

        for row in CURSOR:
            new_item = [
            row[0],
            row[1],
            row[2],
            ]
            data.append(new_item)
        print(data)
        return data

#**************************************************************************#
    def read_done(self ):
        # retuen a list of all pending items
        self.open_db()
        CURSOR = self.conn.execute('''
        SELECT id, description, datecompleted from DONE''')
        data = []

        for row in CURSOR:
            new_item = [
            row[0],
            row[1],
            row[2],
            ]
            data.append(new_item)

        return data
    def remove_done(self, ID):
        # remove a done item with the ID provided
        self.open_db()
        command = f'''
        DELETE from DONE where ID = {ID};
        '''
        self.conn.execute(command)
        print('## deleted DONE ITEM!')
        self.close_db()
    def add_done(self,index,description):
        self.open_db()
        now = datetime.now().strftime("%H:%M  %d-%m-%Y")
        command = f'''
        INSERT INTO DONE(ID,DESCRIPTION,DATECOMPLETED) VALUES(
        {self.allocate_index('DONE')},'{description}','{now}');
    '''
        print(command)
        self.conn.execute(command)


        self.close_db()

#DM = DATAMANAGER()
#DM.open_db()
#DM.add_done(2332,'hgdfhjk')
#done = DM.read_done()
#print(done)
#DATAMANAGER().reset_database()
