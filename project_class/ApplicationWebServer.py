from .WebServer import WebServer
from .simulation_settings import return_web_server_number_cores
import simpy
#TODO: 
# Application webserver consist: 
# 1 webserver nginx
# 1 database
# 1 memcached server

class ApplicationWebServer():
    def __init__(self, env, host_index, out_link, web_server_ip_address):
        self.host_index = host_index
        self.vnfs_number = 3
        self.out_link = out_link
        self.env = env
        self.active = True
        self.web_server_ip_address = web_server_ip_address
        self.in_link = simpy.Store(self.environment)
        self.Webservers = WebServer(env=self.env, out_link=self.out_link, host_index = self.host_index, ip_address= self.web_server_ip_address, in_link=self.in_link)
    
    def ApplicationWebServer_get_ip_address(self):
        return self.web_server_ip_address