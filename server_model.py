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
        self.action = [env.process(self.run(in_pipe=self.in_pipe[i], out_pipe = self.out_pipe[i], index= i)) for i in range(4)]

    #prepare the request to send
    def prepare_request(self):
        processing_time = random.expovariate(1/average_processing_time)
        arrival_time = self.env.now
        self.request = {1: processing_time, 2: self.index, 3: arrival_time}

    # send the request:
    def send_request(self, out_pipe):
        out_pipe.put(self.request)
        pass

    def analyse_response(self, response, index):
        response_time = self.env.now - response[3]
        response_times.append(response_time)
        print("response = " + str(response_time))
        print("index = " + str(index))
        pass

    def run(self, in_pipe, out_pipe, index):
        while True:
            self.prepare_request()
            self.send_request(out_pipe)
            #wait for the request to comeback:
            response = yield in_pipe.get(filter=lambda x: True if x[2] == self.index else False)
            self.analyse_response(response, index)

class Server():
    def __init__(self, env, in_pipe, out_pipe, index):
        self.env = env
        self.out_pipe = out_pipe
        self.in_pipe = in_pipe
        self.processing_time = 0
        self.request = dict()
        self.response = dict()
        self.index = index
        self.action = [env.process(self.run(in_pipe=self.in_pipe[i], out_pipe = self.out_pipe[i])) for i in range(len(in_pipe))]

    #prepare the request to send
    def process_request(self):
        self.processing_time = self.request[1]
        arrival_time = self.request[3]
        waiting_time = self.env.now - arrival_time
        waiting_times.append(waiting_time)
        # queue_length = len(self.in_pipe.items)
        # queue_lengths.append(queue_length)

    # send the request:
    # def prepare_response(self):
    #     yield self.env.timeout(self.processing_time)

    def send_response(self, out_pipe):
        self.response = self.request
        out_pipe.put(self.response)

    def run(self, in_pipe, out_pipe):
        while True:
            #wait for request:
        
            self.request = yield in_pipe.get()
            self.process_request()
            yield self.env.timeout(self.processing_time)
            self.send_response(out_pipe)

random.seed(SEED)

environment = simpy.Environment()
to_server=[simpy.Store(environment) for i in range(4)]
to_client=[simpy.FilterStore(environment) for i in range(4)]
clients = [Client(env=environment, out_pipe=to_server, in_pipe=to_client, index=i) for i in range(concurrency)]
servers = [Server(env=environment, in_pipe=to_server, out_pipe=to_client, index=i) for i in range(num_cores)]
environment.run(100)