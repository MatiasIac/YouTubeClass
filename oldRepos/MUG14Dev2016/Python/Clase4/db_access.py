
import pypyodbc
from user_model import user_model

class database_access(object):
    """Conector a DB"""

    def __init__(self):
        self.connection_string = 'Driver={SQL Server};Server=.;Database=mug;uid=testuser;pwd=testuser'

    def request_rows(self, user_id=None):
        """Retorna filas"""
        db_connection = pypyodbc.connect(self.connection_string)
        cursor = db_connection.cursor()

        if user_id is None:
            cursor.execute("select * from userdata")
        else:
            cursor.execute("select * from userdata where userid=?", (user_id,))

        db_result = cursor.fetchall()

        results = []

        for user in db_result:
            my_model = user_model(user[0], user[1], user[2], user[3])
            results.append(my_model.__dict__)

        db_connection.close()
        return results

    def insert_row(self, user):
        db_connection = pypyodbc.connect(self.connection_string)
        cursor = db_connection.cursor()

        cursor.execute("insert into userdata values(?,?,?)", (user.name, user.lastname, user.age))

        db_connection.commit()
        db_connection.close()

#for model in database_access().request_rows():
#    model.__str__()
