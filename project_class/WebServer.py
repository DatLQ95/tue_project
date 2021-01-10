import simpy
from .Server import Server
from .simulation_settings import return_web_server_number_cores
from .simulation_settings import return_web_server_processing_time

class WebServer():
    def __init__(self, env, application_index, out_link, ip_address):
        self.application_index = application_index
        self.vnfs_number = 3
        self.out_link = out_link
        self.env = env
        self.active = True
        self.ip_address = ip_address
        self.in_link = simpy.Store(self.environment)
        self.processing_time= return_web_server_processing_time()
        self.Webservers = [Server(env=self.env, out_link=self.out_link, index=i, host_index = self.application_index, in_link=self.in_link, processing_time=self.processing_time) for i in range(return_web_server_number_cores())]

        