from project_class.HostMachine import HostMachine

# # def main():


def init():
    # init the host
    # init the links
    host = [HostMachine(cpu=20, memory=100, storage=200, index=i) for i in range(4)]
    
    host[0].get_status()
    host[1].get_status()

    # init the environment 
    # connect the host and links

    pass

def deploy_app():

    pass

def deploy_user():
    pass

def resume_simulation():

    pass

def pause_simulation():

    pass



# if __name__ == '__main__':
#     main()