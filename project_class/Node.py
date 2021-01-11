import simpy
from .simulation_settings import optical_params
from .OpticalWSS1 import WSS1
from .OpticalBuffer import Buffer
from .OpticalCombiner import Combiner
from .OpticalInterface import Interface
from .Link import Link
from .EdgeComputing import EdgeComputing

delay_WSS1_to_Combiner = 1
delay_WSS1_to_Interface = 1
delay_WSS1_to_Buffer = 1
delay_Buffer_to_Combiner = 1
delay_EC_to_Buffer = 1
delay_Interface_to_EC = 1

class Node():
    def __init__(self, env, SC_link_in , data_links_in, SC_link_out, data_links_out, node_index):
        self.node_index = node_index
        self.env = env

        #input link:
        self.SC_link_in = SC_link_in
        self.data_links_in = data_links_in

        #output links:
        self.SC_link_out = SC_link_out
        self.data_links_out = data_links_out
        #TODO: create WSS1, buffer, combiner, interface, sources:
        ### create links:
        # control links:
        SC_link_WSS1_to_buffer = Link(self.env, delay_WSS1_to_Buffer)
        SC_link_buffer_to_combiner = Link(self.env, delay_Buffer_to_Combiner)
        
        # data links:
        data_links_WSS1_to_Interface = [Link(self.env, delay_WSS1_to_Interface) for i in range(optical_params.get_channel_number())]

        data_links_WSS1_to_Combiner = [Link(self.env, delay_WSS1_to_Combiner) for i in range(optical_params.get_channel_number())]

        data_links_Buffer_to_Combiner = [Link(self.env, delay_Buffer_to_Combiner) for i in range(optical_params.get_channel_number())]

        data_links_EC_to_Buffer = [Link(self.env, delay_EC_to_Buffer) for i in range(optical_params.get_TRx_number())]

        data_links_Interface_to_EC = [Link(self.env, delay_Interface_to_EC) for i in range(optical_params.get_TRx_number())]

        ### create function nodes: 
        # WSS1:
        self.wss1 = WSS1(env=self.env, data_links_in= self.data_links_in, links_to_Combiner= data_links_WSS1_to_Combiner, links_to_Interface=data_links_WSS1_to_Interface, SC_link_in=self.SC_link_in, SC_link_out=SC_link_WSS1_to_buffer,node_index= self.node_index)

        #Buffer: 
        self.buffer = Buffer(env=self.env, SC_link_in=SC_link_WSS1_to_buffer, links_from_EC=data_links_EC_to_Buffer, links_to_Combiner=data_links_Buffer_to_Combiner, SC_link_out=SC_link_buffer_to_combiner, node_index =self.node_index)

        #Combiner: 
        self.combiner = Combiner(env= self.env, SC_link_in=SC_link_buffer_to_combiner, links_from_Buffer=data_links_Buffer_to_Combiner, links_from_WSS1=data_links_WSS1_to_Combiner, links_to_WSS1=self.data_links_out, SC_link_out=self.SC_link_out, node_index= self.node_index)

        #Interface: 
        self.interface = Interface(env= self.env, links_to_EC=data_links_Interface_to_EC, links_from_WSS1=data_links_WSS1_to_Interface, node_index= self.node_index)

        #EdgeComputing:
        self.EdgeComputing = EdgeComputing(env=self.env, cpu=20, memory=200, storage=400, node_index=self.node_index, data_links_in=data_links_Interface_to_EC, data_links_out=data_links_EC_to_Buffer)

    def run():

        pass
