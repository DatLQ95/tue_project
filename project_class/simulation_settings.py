import random
### ------------------------------------------------------------------------------
# random parameters
SEED = 42
def random_seed():
    return SEED

### ------------------------------------------------------------------------------
# web server parameters:
web_server_ip_address = 123
def return_web_server_ip_address():
    return web_server_ip_address

web_server_processing_time = 20
def return_web_server_processing_time():
    return web_server_processing_time

web_server_number_cores = 1
def return_web_server_number_cores():
    return web_server_number_cores

web_server_user_ip_address = 100
def return_web_server_user_ip_address():
    return web_server_user_ip_address

### ------------------------------------------------------------------------------
# Optical network: 
Nodes = 4
Channel = 4
load = 0.5
TRx_count = 2

delay_combiner_to_next_WSS1 = 100
delay_WSS1_to_Combiner = 0.43
delay_WSS1_to_Interface = 0.015
delay_WSS1_to_Buffer = 0.015
delay_Buffer_to_Combiner = 0.015
delay_EC_to_Buffer = 0
delay_Interface_to_EC = 0
time_slot = 1
number_control_packets = delay_combiner_to_next_WSS1/time_slot

# buffer[*].timeSlot = 2us
# buffer[*].guardtime = 0.05us
# buffer[*].capacity = 50
# buffer[*].TRx_count = 4
# buffer[*].Rx_count = 4
# WSS1[*].Rx_count = 4
# WSS1[*].timeSlot = 2us
# source[*].load = 0.5
# source[*].TRx_count = 4
# source[*].source_count = 4
# source[*].inter_intra_ratio = 0.5
# #**.Interface[*].load = 0.53
# Interface[*].TRx_count = 4
# Interface[*].source_count = 1

class optical_params():
    def __init__(self):
        pass
        
    def get_node_number():
        return Nodes
    
    def get_channel_number():
        return Channel

    def get_TRx_number():
        return TRx_count
    
    def get_delay_combiner_to_next_WSS1():
        return delay_combiner_to_next_WSS1
    
    def get_delay_WSS1_to_Combiner():
        return delay_WSS1_to_Combiner

    def get_delay_WSS1_to_Interface():
        return delay_WSS1_to_Interface

    def get_delay_WSS1_to_Buffer():
        return delay_WSS1_to_Buffer

    def get_delay_Buffer_to_Combiner():
        return delay_Buffer_to_Combiner

    def get_delay_EC_to_Buffer():
        return delay_EC_to_Buffer

    def get_delay_Interface_to_EC():
        return delay_Interface_to_EC
