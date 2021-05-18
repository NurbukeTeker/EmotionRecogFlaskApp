class User(object):
    
    def __init__(self,usermail):
        self.usermail = usermail
        self.isIn = False
       
    def update(self):
        self.isIn = True
    
    def userisIn(self):
        if self.isIn:
            return True
        else:
            return False