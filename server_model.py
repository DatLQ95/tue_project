import random
import simpy
import numpy as np
import matplotlib.pyplot as plt

SEED = 42
average_processing_time = 25

response_times =[]
queue_lengths = []
waiting_times = []

concurrency = 100
num_cores = 4

class Client():
    # initial with parameters:
    def __init__(self, env, out_pipe, in_pipe, index):
        self.env = env
        self.out_pipe = out_pipe
        self.in_pipe = in_pipe
        self.index = index
        self.request = dict()
        self.action = env.process(self.run())

    #prepare the request to send
    def prepare_request(self):
        processing_time = random.expovariate(1/average_processing_time)
        arrival_time = self.env.now
        self.request = {1: processing_time, 2: self.index, 3: arrival_time}

    # send the request:
    def send_request(self):
        self.out_pipe.put(self.request)
        pass

    def analyse_response(self, response):
        response_time = self.env.now - response[3]
        response_times.append(response_time)
        pass

    def run(self):
        while True:
            self.prepare_request()
            self.send_request()
            #wait for the request to comeback:
            response = yield self.in_pipe.get(filter=lambda x: True if x[2] == self.index else False)
            self.analyse_response(response)

class Server():
    def __init__(self, env, in_pipe, out_pipe, index):
        self.env = env
        self.out_pipe = out_pipe
        self.in_pipe = in_pipe
        self.processing_time = 0
        self.request = dict()
        self.response = dict()
        self.index = index
        self.action = env.process(self.run())

    #prepare the request to send
    def process_request(self):
        self.processing_time = self.request[1]
        arrival_time = self.request[3]
        waiting_time = self.env.now - arrival_time
        waiting_times.append(waiting_time)
        queue_length = len(self.in_pipe.items)
        queue_lengths.append(queue_length)

    # send the request:
    # def prepare_response(self):
    #     yield self.env.timeout(self.processing_time)

    def send_response(self):
        self.response = self.request
        self.out_pipe.put(self.response)

    def run(self):
        while True:
            #wait for request:
        
            self.request = yield self.in_pipe.get()
            self.process_request()
            yield self.env.timeout(self.processing_time)
            self.send_response()

random.seed(SEED)

environment = simpy.Environment()
to_server=simpy.Store(environment)
to_client=simpy.FilterStore(environment)
clients = [Client(env=environment, out_pipe=to_server, in_pipe=to_client, index=i) for i in range(concurrency)]
servers = [Server(env=environment, in_pipe=to_server, out_pipe=to_client, index=i) for i in range(num_cores)]
environment.run(100000)