class WSS1():
    def __init__(self, env, data_links_in, SC_link_in, links_to_Interface, links_to_Combiner, SC_link_out):
        self.env = env
        self.data_links_in = data_links_in
        self.links_to_Interface = links_to_Interface
        self.links_to_Combiner = links_to_Combiner
        self.SC_link_in = SC_link_in
        self.SC_link_out = SC_link_out

    def control_packet_handler(self, parameter_list):
        """
        docstring
        """
        pass

    def data_packet_handler(parameter_list):
        """
        docstring
        """
        pass
    


