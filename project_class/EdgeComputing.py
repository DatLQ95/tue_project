import random

import simpy
from .Packet import Packet
from .simulation_settings import random_seed


#TODO: consider to use container as host machine
class EdgeComputing():
    def __init__(self, env, cpu, memory, storage, node_index, data_links_in, data_links_out):
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.node_index = node_index
        self.vnfs_number = 0
        self.data_links_in = data_links_in
        self.data_links_out = data_links_out
        self.env = env
        self.active = True
        self.request = Packet()
        self.active = True
        self.vnfs = dict()
        self.get_packet_instance = [env.process(self.get_packet(data_in_link=i)) for i in self.data_links_in]
        # self.send_packet_instance = [env.process(self.send_packet(data_link_out=i)) for i in self.data_links_out]

    # #prepare the request to send
    def process_request(self, request):
        if(request.packet_get_dst() == self.node_index):
            print("Got it bro!!!")
            time_taken = self.env.now - request.packet_get_arrival_time()
            print(time_taken)
    
    def send_packet(self, data_link_out):
        for i in range(1000):
            if(self.node_index == 2):
                packet = Packet(dst=1,src=self.node_index, arrival_time=self.env.now)
                data_link_out.put(packet)
                yield self.env.timeout(1)


    def get_packet(self, data_in_link):
        while (self.active):
            # wait for request:
            request = yield data_in_link.get()
            self.process_request(request)
            # self.send_response(out_link=self.out_link, response=self.request)
