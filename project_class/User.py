class User():
    # initial with parameters:
    def __init__(self, env, out_pipe, in_pipe, index):
        pass
        self.env = env
        self.out_pipe = out_pipe
        self.in_pipe = in_pipe
        self.index = index
        self.action = env.process(self.run())
        self.request = Packet()

    #prepare the request to send
    def prepare_request(self):
        pass
        # processing_time = random.expovariate(1/average_processing_time)
        # arrival_time = self.env.now
        # self.request.packet_set_processing_time(processing_time)
        # self.request.packet_set_index(self.index)
        # self.request.packet_set_arrival_time(arrival_time)

    # send the request:
    def send_request(self):
        pass
        # self.out_pipe.put(self.request)

    def analyse_response(self, response):
        pass
        # response_time = self.env.now - response.packet_get_arrival_time()
        # response_times.append(response_time)

    def run(self):
        pass
        # while True:
        #     self.prepare_request()
        #     self.send_request()
        #     print("process = " + str(self.request.packet_get_processing_time()))
        #     print("index = " + str(self.request.packet_get_index()))
        #     print("arrival =" + str(self.request.packet_get_arrival_time()))
            
        #     #wait for the request to comeback:
        #     response = yield self.in_pipe.get(filter=lambda x: True if x.packet_get_index() == self.index else False)
        #     self.analyse_response(response)