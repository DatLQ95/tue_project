from project_class.Link import Link
from project_class.ApplicationWebServer import ApplicationWebServer
from project_class.simulation_settings import return_web_server_ip_address
from project_class.simulation_settings import return_web_server_user_ip_address
from project_class.simulation_settings import optical_params
from project_class.Node import Node

import simpy

delay_combiner_to_next_WSS1 = 100

class Simulation():
    def __init__(self):
        # init the environment 
        self.environment = simpy.Environment()

        # delay_WSS= 100
        # init the network:
        ### TODO: create links, nodes:
        #FIXME: 
        # SC_links = [Link(env=self.environment, delay_time= delay_WSS) for  i in range(optical_params.get_node_number())]

        # data_links = [[Link(env=self.environment, delay_time= delay_WSS) for j in range(optical_params.get_channel_number())] for  i in range(optical_params.get_node_number())]
        
        # TODO: create links: 
        SC_links = [Link(env=self.environment, delay_time= delay_combiner_to_next_WSS1) for  i in range(optical_params.get_node_number())]

        data_links = [[Link(env=self.environment, delay_time= delay_combiner_to_next_WSS1) for j in range(optical_params.get_channel_number())] for  i in range(optical_params.get_node_number())]
        # TODO: create nodes: 
        nodes = [Node(env= self.environment, SC_link_in= SC_links[i], data_links_in= data_links[i], SC_link_out= SC_links[i+1], data_links_out= data_links[i+1], node_index= i) for i in range(optical_params.get_node_number() - 1)]

        nodes.append(Node(env= self.environment,SC_link_in= SC_links[optical_params.get_node_number()- 1], data_links_in= data_links[optical_params.get_node_number()- 1], SC_link_out= SC_links[0], data_links_out= data_links[0], node_index= optical_params.get_node_number()- 1))
        # Run control packet init


    #TODO: : init the whole optical parts of the network:
    def init_network(self):
        
        pass

    #TODO: parameters: which application and which host machine to deploy! 
    def deploy_app(self):
        #FIXME: Test to deploy web server to host 3!
        

        pass

    def deploy_user(self):   
        
        pass

    def resume_simulation():

        pass

    def pause_simulation():

        pass

    def simulation_result():

        pass
    # FIXME: test ping:
    def send_ping():

        pass

    def simulation_run(self):
        self.environment.run(1000)

    # if __name__ == '__main__':
    #     main()
    
# user = UserBehavior()

simulation = Simulation()

# simulation.deploy_user(user)

simulation.simulation_run()
