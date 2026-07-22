from datetime import datetime
# print(datetime.now())
class base :
    def __init__(self):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def get_user_register_age(self):
        return datetime.now() - self.created_at
