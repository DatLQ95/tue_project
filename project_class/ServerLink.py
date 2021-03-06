import random
from .Packet import Packet
from .simulation_settings import random_seed

class ServerLink():
    def __init__(self, env, in_link, out_link, index, link_index, delay_link):
        random.seed(random_seed())
        self.env = env
        self.out_link = out_link
        self.in_link = in_link
        self.processing_time = 0
        self.request = Packet()
        self.index = index
        self.action = env.process(self.run())
        self.active = True
        self.link_index = link_index
        # FIXME:
        # self.delay_link = random.expovariate(1/delay_link)
        self.delay_link = delay_link
    #prepare the request to send
    def process_request(self):
        # go to application in machine host or not!
        # check if the packet belongs to application in this host
        # if it is, send response to the server
        # if it not, pass message to the output link
        # if(self.request.packet_)
        pass
        
    def send_response(self, out_link, response):
        out_link.put(response)
        pass

    def run(self):
        while (self.active):
            #wait for request:
            print("in link " + str(self.link_index))
            self.request = yield self.in_link.get()
            yield self.env.timeout(self.delay_link)
            
            print("in link time " + str(self.env.now))
            # self.process_request()
            self.send_response(out_link=self.out_link, response=self.request)
        