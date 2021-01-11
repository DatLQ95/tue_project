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
TRx_count = 4


time_slot = 1
# number_control_packets = delay_combiner_to_next_WSS1/time_slot

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
    def __init__(self= None):
        pass
        
    def get_node_number(self=None):
        return Nodes
    
    def get_channel_number(self=None):
        return Channel

    def get_TRx_number(self=None):
        return TRx_count
