from .simulation_settings import optical_params

class WSS1():
    def __init__(self, env, data_links_in, SC_link_in, links_to_Interface, links_to_Combiner, SC_link_out, node_index):
        self.env = env
        self.data_links_in = data_links_in
        self.links_to_Interface = links_to_Interface
        self.links_to_Combiner = links_to_Combiner
        self.SC_link_in = SC_link_in
        self.SC_link_out = SC_link_out
        self.node_index = node_index
        self.active = True
        self.get_packet_instance = [env.process(self.data_packet_handler(data_in_link=i)) for i in self.data_links_in]
        self.get_control_packet_instance = env.process(self.control_packet_handler(SC_link_in= self.SC_link_in, SC_link_out= self.SC_link_out))
        self.permit_to_send = [False for i in range(optical_params.get_channel_number())]

    def send_data(self, data_links_out, packet):
        data_links_out.put(packet)
        pass

    # #prepare the request to send
    def process_request(self, packet):
        print("in WSS1 " + str(self.node_index))
        if(self.permit_to_send[packet.packet_get_channel_index()]):
            print("send to Interface")
            self.send_data(data_links_out=self.links_to_Interface[0], packet=packet)
        else: 
            print("send to combiner")
            self.send_data(data_links_out=self.links_to_Combiner[0], packet=packet)
    

    def data_packet_handler(self, data_in_link):
        """
        send the packet arrival to the buffer
        """
        while (self.active):
            # wait for request:
            request = yield data_in_link.get()
            self.process_request(packet=request)

    def process_control_packet(self, control_packet, SC_link_out):
        """
        process the control packet
        check the control packet dst is here or not
        """
        rx_to_connect = 0
        print("Got the control packet at " + str(self.env.now))
        dst_table = control_packet.packet_get_dst_table()
        for i in dst_table:
            if (i == self.node_index):
                if (rx_to_connect < optical_params.get_TRx_number()):
                    self.permit_to_send[i] = True
                    dst_table[i] = -1
                    rx_to_connect = rx_to_connect + 1
        
        control_packet.packet_set_dst_table(dst_table)
        SC_link_out.put(control_packet)

    def control_packet_handler(self, SC_link_in, SC_link_out):
        """
        change the control packet
        assign the data packet to wavelength based on length of buffers
        send the data via wavelength assignment
        """
        while (self.active):
            # wait for request:
            control_packet = yield SC_link_in.get()
            self.process_control_packet(control_packet=control_packet, SC_link_out= SC_link_out)
        pass
