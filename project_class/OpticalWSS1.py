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

    def send_control_packets(self):
        # send 100 control packets
        pass

    def send_data(self, data_links_out, packet):
        data_links_out.put(packet)
        pass

    # #prepare the request to send
    def process_request(self, packet):
        print("in WSS1 " + str(self.node_index))
        if(packet.packet_get_dst() == self.node_index):
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


    def control_packet_handler(self):
        """
        change the control packet
        assign the data packet to wavelength based on length of buffers
        send the data via wavelength assignment
        """
        pass
