# Control all the user activities
from .User import User
import simpy

class UserWebserver():
    def __init__(self, env, user_number = None, user_pattern = None, application = None, out_link = None, host_index = None, ip_address = None, server_ip = None):
        self.user_pattern = user_pattern 
        self.user_number = user_number
        self.application = application
        self.env = env
        self.out_link = out_link
        self.in_link = simpy.FilterStore(self.env)
        self.ip_address = ip_address
        self.server_ip = server_ip
        self.Users = [User(env=self.env, out_link=self.out_link, in_link=self.in_link, index=i, application_process_time= self.application, ip_src=ip_address, ip_dst=self.server_ip) for i in range(self.user_number)]
        self.host_index = host_index

    def UserWebServer_get_ip_address(self):
        return self.ip_address

    def UserWebServer_get_in_link(self):
        return self.in_link


        

