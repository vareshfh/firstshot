# from datetime import datetime
# # print(datetime.now())
# class base :
#     def __init__(self):
#         self.created_at = datetime.now()
#         self.updated_at = datetime.now()
#     def get_user_register_age(self):
#         return datetime.now() - self.created_at

from utils import base
class users(base) :
    def __init__(self,**fields):
        self.fields= fields
        super().__init__()
    
    def __str__(self):
        print(self.created_at)
        print(self.updated_at)
        for key,value in self.fields.items():
            print(key, " = ", value)
        return ""
    def __eq__(self, obj):
        return (self.fields == obj.fields)

a=base()
# print(a.created_at)
user1 = users(name="Ali",family="alizade",job= "teacher")
user2 = users(name="Ali",family="alizade",job= "teacher")
user3 = user1
print(user1 == user2)
print(user1 == user3)


