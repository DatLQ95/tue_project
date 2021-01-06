# Control all the user activities
from .User import User

class UserBehavior():
    def __init__(self, env, user_number = None, user_pattern = None, application = None, out_link = None, in_link = None, host_index = None):
        self.user_pattern = user_pattern 
        self.user_number = user_number
        self.application = application
        self.env = env
        self.in_link = in_link
        self.out_link = out_link
        self.Users = [User(env=self.env, out_link=self.out_link, in_link=self.in_link, index=i, application_process_time= self.application) for i in range(self.user_number)]
        self.host_index = host_index
        

