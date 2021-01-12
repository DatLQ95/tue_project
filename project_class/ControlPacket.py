from .Packet import Packet

class ControlPacket(Packet):
    def __init__(self, dst, src, start_time, dst_table):
        super().__init__(dst=dst, src=src, start_time=start_time)
        self.dst_table = dst_table

    def packet_set_dst_table(self, dst):
        self.dst_table = dst
    
    def packet_get_dst_table(self):
        return self.dst_table