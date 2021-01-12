from .Packet import Packet
from .ControlPacket import ControlPacket
import simpy
from .simulation_settings import optical_params

class Buffer():
    def __init__(self, env, SC_link_in, links_from_EC, links_to_Combiner, SC_link_out, node_index):
        self.env = env
        self.node_index = node_index
        self.SC_link_in = SC_link_in
        self.SC_link_out = SC_link_out
        self.links_to_Combiner = links_to_Combiner
        self.links_from_EC = links_from_EC
        self.active = True
        self.packet_loss = 0
        self.TX_buffers = [simpy.Store(self.env, capacity= optical_params.get_buffer_capacity()) for i in range(optical_params.get_TRx_number())]
        self.get_packet_instance = [env.process(self.data_packet_handler(data_in_link=self.links_from_EC[i], TX_buffer=self.TX_buffers[i])) for i in range(len(self.links_from_EC))]
        self.sendControlPackets = env.process(self.send_init_control_packets(data_link_out=self.SC_link_out))

    def send_data(self, data_links_out, packet):
        data_links_out.put(packet)
        pass

    def data_packet_handler(self, data_in_link, TX_buffer):
        """
        send the packet arrival to the buffer
        """
        while (self.active):
            # wait for request:
            data_packet = yield data_in_link.get()
            # check if the length of the buffer is reached?
            if(len(TX_buffer.items) > optical_params.get_buffer_capacity()):
                # if buffer is full then we increase packet loss
                self.packet_loss = self.packet_loss + 1
            else: 
                # put it into the buffer
                TX_buffer.put(data_packet)
                # for te
                # self.send_data(data_links_out=self.links_to_Combiner[0], packet=packet)


    def return_packet_loss(self):
        return self.packet_loss

    def send_init_control_packets(self,data_link_out):
        # send 100 control packets
        for i in range(optical_params.get_number_control_packet()):
            dst_table = [-1 for i in range(optical_params.get_channel_number())]
            control_packet = ControlPacket(dst=1, src=self.node_index, start_time=self.env.now, dst_table=dst_table)
            data_link_out.put(control_packet)
            yield self.env.timeout(optical_params.get_time_slot())

    def process_control_packet(self, control_packet, SC_link_out):
        """
        process the control packet
        check the longest buffer and free channels then assign the longest to the free channel
        """
        # sorting: 
        buffer_dict = dict()
        for i in self.TX_buffers:
            buffer_dict[i] = len(i.items)
        sorted(buffer_dict.items(), key = lambda kv:(kv[1]), reverse= True)
        dst_table = control_packet.packet_get_dst_table()
        count = 0
        for i in dst_table:
            if (i == -1):

        pass

    def control_packet_handler(self, SC_link_in, SC_link_out):
        """
        change the control packet
        assign the data packet to wavelength based on length of buffers
        send the data via wavelength assignment
        set packet channel index to sent packet
        """
        while (self.active):
            # wait for request:
            control_packet = yield SC_link_in.get()
            self.process_control_packet(control_packet=control_packet, SC_link_out= SC_link_out)
        pass



    

    


    