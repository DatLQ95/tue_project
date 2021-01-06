import simpy
from .ServerLink import ServerLink

class HostMachine():
    def __init__(self, env, cpu, memory, storage, index, in_link, out_link, bw):
        self.cpu = cpu
        self.memory = memory
        self.storage = storage
        self.index = index
        self.vnfs_number = 0
        self.in_link = in_link
        self.out_link = out_link
        self.env = env
        self.active = True
        self.bandwidth = bw
        self.delay_link = 10
        self.LinkServers = [ServerLink(env=self.env, in_link=self.in_link, out_link=self.out_link, index=i, host_index = self.index, delay_link=self.delay_link) for i in range(self.bandwidth)]
        

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
