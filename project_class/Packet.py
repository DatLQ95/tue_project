class Packet():
    def __init__(self, dst = None, src = None, app = None, processing_time = None, index = None, arrival_time =None):
        self.dst = dst
        self.src = src
        self.application = app
        self.arrival_time = arrival_time
        self.processing_time = processing_time
        self.index = index

    def packet_get_dst(self):
        return self.dst

    def packet_get_src(self):
        return self.src

    def packet_get_application(self):
        return self.application

    def packet_get_arrival_time(self):
        return self.arrival_time

    def packet_get_processing_time(self):
        return self.processing_time

    def packet_get_index(self):
        return self.index

    def packet_set_processing_time(self, processing_time):
        self.processing_time = processing_time

    def packet_set_index(self, index):
        self.index = index

    def packet_set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_packet_detail(self):
        print("src: "+ str(self.src))