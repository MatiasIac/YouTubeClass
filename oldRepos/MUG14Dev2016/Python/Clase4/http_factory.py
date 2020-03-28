
from db_access import database_access
from user_model import user_model
import simplejson

class http_factory(object):

    def __init__(self):
        self.function_pointers = {
            'get_users': self.get_users,
            'post_users': self.post_users
        }

    def get_users(self, params):
        user_id = None

        if len(params) > 1:
            user_id = params[1]

        rows = database_access().request_rows(user_id=user_id)
        return simplejson.dumps(rows)

    def post_users(self, json_string):
        data = simplejson.loads(json_string)
        user = user_model(None, data["name"], data["lastname"], data["age"])
        database_access().insert_row(user=user)


#factory = http_factory()
#factory.function_pointers.get('get_' + 'users')()
