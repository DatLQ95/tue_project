class Packet():
    def __init__(self, dst = None, src = None, start_time =None):
        self.dst = dst
        self.src = src
        self.start_time = start_time

    def packet_get_dst(self):
        return self.dst

    def packet_set_dst(self, dst):
        self.dst = dst

    def packet_get_src(self):
        return self.src
    
    def packet_set_src(self, src):
        self.src = src

    def packet_get_arrival_time(self):
        return self.start_time

    def packet_set_processing_time(self, processing_time):
        self.processing_time = processing_time

    def packet_set_index(self, index):
        self.index = index

    def packet_set_arrival_time(self, start_time):
        self.arrival_time = start_time

    def get_packet_detail(self):
        print("src: "+ str(self.src))