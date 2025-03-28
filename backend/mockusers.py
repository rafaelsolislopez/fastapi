import users

class MockUsers():
    def __init__(self):
        self.user1=User(id=1,name="Rafa",mail="rafa@mail.com",age=41)
        self.user2=User(id=2,name="Leo",mail="leo@mail.com",age=9)
        self.user3=User(id=3,name="jorge",mail="gorge@mail.com",age=6)

    def get_user_list(self)->list:
        user_list=[self.user1,self.user2,self.user3]
        return user_list
    
    def new_user(self,id:int)->User:
        self.user=User(id=id,name=f"Name{id}",mail="name{id}@mail.com",age=id*5)
        return self.user
    