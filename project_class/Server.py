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
        pass
        # self.processing_time = self.request[1]
        # arrival_time = self.request[3]
        # waiting_time = self.env.now - arrival_time
        # waiting_times.append(waiting_time)
        # queue_length = len(self.in_pipe.items)
        # queue_lengths.append(queue_length)

    # send the request:
    # def prepare_response(self):
    #     yield self.env.timeout(self.processing_time)

    def send_response(self):
        pass
        # self.response = self.request
        # self.out_pipe.put(self.response)

    def run(self):
        pass
        # while True:
        #     #wait for request:
        #     self.request = yield self.in_pipe.get()
        #     self.process_request()
        #     yield self.env.timeout(self.processing_time)
        #     self.send_response()