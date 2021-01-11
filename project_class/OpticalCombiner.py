class Combiner():
    def __init__(self, env, SC_link_in, links_from_Buffer, links_from_WSS1, links_to_WSS1, SC_link_out, node_index):
        self.env = env
        self.node_index = node_index
        # self.SC_link_in = SC_link_in
        # self.SC_link_out = SC_link_out
        # self.links_from_Buffer = links_from_Buffer
        # self.links_from_WSS1 = links_from_WSS1
        # self.links_to_WSS1 = links_to_WSS1
        self.active = True
        self.process1 = self.env.process(self.run(in_link=SC_link_in, out_link = SC_link_out))
        self.process2 = [self.env.process(self.run(in_link=links_from_Buffer[i], out_link=links_to_WSS1[i])) for i in range(len(links_to_WSS1))]
        self.process3 = [self.env.process(self.run(in_link=links_from_WSS1[i], out_link=links_to_WSS1[i])) for i in range(len(links_to_WSS1))]

    def run(self, in_link, out_link):
        while (self.active):
            packet = yield in_link.get()
            print("in combiner " +str(self.node_index))
            # yield self.env.timeout(delay_time)
            out_link.put(packet)
            
        
