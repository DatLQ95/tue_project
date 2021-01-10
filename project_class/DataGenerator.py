import simpy
import random
from .simulation_settings import random_seed
from .Packet import Packet

class DataGenerator():
    def __init__(self, env, out_link, index, application_process_time):
        random.seed(random_seed())
        self.env = env
        self.out_link = out_link
        self.in_link = simpy.FilterStore(self.env)
        self.index = index
        self.action = env.process(self.run())
        self.request = Packet()
        self.application_process_time = application_process_time

    #prepare the request to send
    def prepare_request(self):
        processing_time = random.expovariate(1/self.application_process_time)
        arrival_time = self.env.now
        self.request.packet_set_processing_time(processing_time)
        self.request.packet_set_index(self.index)
        self.request.packet_set_arrival_time(arrival_time)

    # send the request:
    def send_request(self):
        self.out_link.put(self.request)

    def analyse_response(self, response):
        response_time = self.env.now - response.packet_get_arrival_time()
        print("return time " + str(self.env.now))
        print("return start time" + str(response.packet_get_arrival_time()))
        print("return " + str(response_time))
        # response_times.append(response_time)

    def get_in_link(self):
        return self.in_link

    def run(self):
        # while True:
            self.prepare_request()
            self.send_request()
            #wait for the request to comeback:
            # FIXME:
            # response = yield self.in_link.get(filter=lambda x: True if x.packet_get_index() == self.index else False)
            response = yield self.in_link.get()
            
            self.analyse_response(response)
            # print("process = " + str(self.request.packet_get_processing_time()))
            # print("index = " + str(self.request.packet_get_index()))
            # print("arrival =" + str(self.request.packet_get_arrival_time()))