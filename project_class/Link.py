import simpy

class Link(object):
    """This class represents the propagation through a optical link."""
    def __init__(self, env, delay_time):
        self.env = env
        self.delay_time = delay_time
        self.store = simpy.Store(env)

    def latency(self, value, delay_time):
        yield self.env.timeout(delay_time)
        self.store.put(value)

    def put(self, value):
        self.env.process(self.latency(value, self.delay_time))

    def get(self):
        return self.store.get()