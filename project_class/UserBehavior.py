# Control all the user activities
from User import User

class UserBehavior():
    def __init__(self, env, user_number = None, user_pattern = None):
        self.user_pattern = user_pattern 
        self.user_number = user_number
        self.application
        self.env = env
        pass

    def run(self):
        clients = [Client(env=environment, out_pipe=to_server, in_pipe=to_client, index=i) for i in range(concurrency)]


