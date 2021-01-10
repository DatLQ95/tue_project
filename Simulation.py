from project_class.HostMachine import HostMachine
from project_class.UserBehavior import UserWebserver
from project_class.Link import Link
from project_class.ApplicationWebServer import ApplicationWebServer
from project_class.simulation_settings import return_web_server_ip_address
from project_class.simulation_settings import return_web_server_user_ip_address

import simpy

class Simulation():
    def __init__(self):
        # init the environment 
        self.environment = simpy.Environment()


        # init the network:
        #TODO: create links, WSS1, Buffer, Interface, Combiner, Source
        # Run control packet init

        
        

    #TODO: : init the whole optical parts of the network:
    def init_network(self):
        # TODO: create nodes: 
        pass

    #TODO: parameters: which application and which host machine to deploy! 
    def deploy_app(self):
        #FIXME: Test to deploy web server to host 3!
        self.app_web_server = ApplicationWebServer(env= self.environment, host_index= 2, out_link= self.host[2].HostMachine_get_out_link(), ip_address= return_web_server_ip_address())

        self.host_2.HostMachine_deploy_application(self.app_web_server.ApplicationWebServer_get_ip_address())

        self.user_web_server = UserWebserver(env= self.environment, user_number=1, out_link=self.link_0_1_0, host_index=0, ip_address=return_web_server_user_ip_address(), server_ip= self.app_web_server.ApplicationWebServer_get_ip_address())

        self.host_0.HostMachine_deploy_application(self.user_web_server.UserWebServer_get_ip_address())

        pass

    def deploy_user(self):   
        
        pass

    def resume_simulation():

        pass

    def pause_simulation():

        pass

    def simulation_result():

        pass

    def simulation_run(self):
        self.environment.run(200)

    # if __name__ == '__main__':
    #     main()
    
# user = UserBehavior()

simulation = Simulation()

# simulation.deploy_user(user)

simulation.simulation_run()
