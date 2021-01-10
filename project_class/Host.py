import random
from .Packet import Packet
from .simulation_settings import random_seed

class Host():
    def __init__(self, env, in_link, out_link, index, host_index, delay_link):
        random.seed(random_seed())
        self.env = env
        self.out_link = out_link
        self.in_link = in_link
        self.processing_time = 0
        self.request = Packet()
        self.index = index
        self.action = env.process(self.run())
        self.active = True
        self.host_index = host_index

    #prepare the request to send
    def process_request(self):
        # go to application in machine host or not!
        # check if the packet belongs to application in this host
        # if it is, send response to the server
        # if it not, pass message to the output link
        # if(self.request.packet_)
        if(self. self.request.packet_get_application())
        pass
        
    def send_response(self, out_link, response):
        out_link.put(response)
        pass

    def run(self):
        while (self.active):
            #wait for request:
            print("in host " + str(self.host_index))
            self.request = yield self.in_link.get()
            print("in host time " + str(self.env.now))
            self.send_response(out_link=self.out_link, response=self.request)
        