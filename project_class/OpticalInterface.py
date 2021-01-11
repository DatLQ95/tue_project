class Interface():
    def __init__(self, env, links_to_EC, links_from_WSS1, node_index):
        self.node_index = node_index
        self.env = env
        self.links_to_EC = links_to_EC
        self.links_from_WSS1 = links_from_WSS1
        self.active = True
        self.get_packet_instance = [env.process(self.data_packet_handler(data_in_link=i)) for i in self.links_from_WSS1]

    def send_control_packets(self):
        # send 100 control packets
        pass

    def send_data(self, data_links_out, packet):
        data_links_out.put(packet)
        pass

    # #prepare the request to send
    def process_request(self, packet):
        print("In Interface")
        if(packet.packet_get_dst() == self.node_index):
            print("Send to EC")
            self.send_data(data_links_out=self.links_to_EC[0], packet=packet)
        else: 
            print("Fail here ")
    

    def data_packet_handler(self, data_in_link):
        """
        send the packet arrival to the buffer
        """
        while (self.active):
            # wait for request:
            request = yield data_in_link.get()
            self.process_request(packet=request)
