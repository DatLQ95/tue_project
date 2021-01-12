from .Packet import Packet

class DataPacket(Packet):
    def __init__(self, dst, src, start_time, channel_index = None):
        super().__init__(dst=dst, src=src, start_time=start_time)
        self.channel_index = channel_index

    def packet_set_channel_index(self, channel_index):
        self.channel_index = channel_index
    
    def packet_get_channel_index(self):
        return self.channel_index