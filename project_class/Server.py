import simpy
import random
from .Packet import Packet
from .simulation_settings import random_seed

class Server():
    def __init__(self, env, out_link, index, ip_address, in_link, processing_time):
        random.seed(random_seed())
        self.env = env
        self.out_link = out_link
        self.processing_time = 0
        self.request = Packet()
        self.index = index
        self.action = env.process(self.run())
        self.in_link = in_link
        self.active = True
        self.ip_address = ip_address
        self.process_time = random.expovariate(1/processing_time)

    def webServer_get_in_link(self):
        return self.in_link

    def process_request(self):
        pass
        
    def send_response(self, out_link, response):
        out_link.put(response)
        pass

    def run(self):
        while (self.active):
            #wait for request:
            print("in web server " + str(self.link_index))
            self.request = yield self.in_link.get()
            yield self.env.timeout(self.process_time)
            print("in web server time " + str(self.env.now))
            self.send_response(out_link=self.out_link, response=self.request)
        