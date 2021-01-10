from .Packet import Packet

class Buffer():
    def __init__(self, env, SC_link_in, links_from_EC, links_to_Combiner, SC_link_out):
        self.env = env
        self.SC_link_in = SC_link_in
        self.SC_link_out = SC_link_out
        self.links_to_Combiner = links_to_Combiner
        self.links_from_EC = links_from_EC
        self.active = True


    def send_control_packets(self):
        # send 100 control packets
        pass

    def data_packet_handler(self):
        """
        send the packet arrival to the buffer
        """
        pass

    def control_packet_handler(self):
        """
        change the control packet
        assign the data packet to wavelength based on length of buffers
        send the data via wavelength assignment
        """
        pass

    