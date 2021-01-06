from project_class.HostMachine import HostMachine
from project_class.UserBehavior import UserBehavior
import simpy

class Simulation():
    def __init__(self):
        # init the environment 

        self.environment = simpy.Environment()
        # link1=simpy.Store(environment)
        # init the links
        self.link_0_to_1=simpy.FilterStore(self.environment)
        self.link_1_to_2=simpy.FilterStore(self.environment)
        self.link_2_to_3=simpy.FilterStore(self.environment)
        self.link_3_to_0=simpy.FilterStore(self.environment)
        # init the host
        # connect the host and links
        self.host0 = HostMachine(env=self.environment, cpu=20, memory=100, storage=200, index=0, in_link=self.link_3_to_0, out_link=self.link_0_to_1, bw=1)

        self.host1 = HostMachine(env=self.environment, cpu=20, memory=100, storage=200, index=1, in_link=self.link_0_to_1, out_link=self.link_1_to_2, bw=1)

        self.host2 = HostMachine(env=self.environment, cpu=20, memory=100, storage=200, index=2, in_link=self.link_1_to_2, out_link=self.link_2_to_3, bw=1)

        self.host3 = HostMachine(env=self.environment, cpu=20, memory=100, storage=200, index=3, in_link=self.link_2_to_3, out_link=self.link_3_to_0, bw=1)

        self.user0 = UserBehavior(env= self.environment, user_number= 100, application=20, out_link= self.link_0_to_1, in_link=self.link_3_to_0, host_index=0)

        # host = [HostMachine(cpu=20, memory=100, storage=200, index=i, ) for i in range(4)]
        # host[0].get_status()
        # host[1].get_status()
        # 
        # self.user0 = UserBehavior()

    # def host1pinghost3(self):
    #     UserBehavior = UserBehavior()

    def deploy_app():
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
        self.environment.run(10000)

    # if __name__ == '__main__':
    #     main()

simulation = Simulation()
simulation.simulation_run()
