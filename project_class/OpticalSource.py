from .Packet import Packet

class OpticalSource():
    def __init__(self):
        self.active = True
        pass
    
    # Send packet to buffer 
    def SendPacket(self):
        while (self.isActive):
            packet = Packet(dst = 1, src=self.node)
            
    

