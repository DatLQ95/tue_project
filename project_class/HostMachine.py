import random
from .Packet import Packet
from .simulation_settings import random_seed


#TODO: consider to use container as host machine
class HostMachine():
    def __init__(self, env, cpu, memory, storage, index, in_link, out_link):
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.index = index
        self.vnfs_number = 0
        self.in_link = in_link
        self.out_link = out_link
        self.env = env
        self.active = True
        random.seed(random_seed())
        self.request = Packet()
        self.action = env.process(self.run())
        self.active = True
        self.vnfs = dict()

    def deploy_application(self):
        #deploy the application
        pass

    def remove_application(self):
        pass

    def get_status(self):
        print("Host machine " + str(self.index))
        print("CPU " + str(self.cpu))
        print("storage " + str(self.storage) +"\n")

        pass

    def set_pause(self):
        self.active = False

    def set_active(self):
        self.active = True

    def HostMachine_get_out_link(self):
        return self.out_link

    #prepare the request to send
    def process_request(self):
        # go to application in machine host or not!
        # check if the packet belongs to application in this host
        # if it is, send response to the server
        # if it not, pass message to the output link
        # if(self.request.packet_)
        # if(self. self.request.packet_get_application())
        pass
        
    def send_response(self, out_link, response):
        out_link.put(response)
        pass

    def HostMachine_deploy_application(self, application_ip_address, in_link):
        self.vnfs[application_ip_address] = in_link
        pass

    def HostMachine_contain_ip_address(self, application_ip_address):
        if application_ip_address in self.vnfs.keys : 
            return self.vnfs[application_ip_address]
        else :
            return False
    


    def run(self):
        while (self.active):
            #wait for request:
            self.request = yield self.in_link.get()
            self.process_request()
            # self.send_response(out_link=self.out_link, response=self.request)
