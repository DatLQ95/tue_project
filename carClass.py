import simpy


class Car(object):
    def __init__(self, env, name, links) -> None:
        super().__init__()
        self.env = env
        self.links = links
        self.action1 = [env.process(self.run1()) for i in range(2)]
        self.name = name

    def run1(self):
        while True:
            print(self.name, "parrk run 1 %d" % self.env.now)
            charge_duration = 5
            yield self.env.process(self.charge(charge_duration))

            print(self.name, "star driving 1 %d" % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)

    
    def charge(self, duration):
        yield self.env.timeout(duration)

env = simpy.Environment()
link = [simpy.FilterStore(env) for i in range(3)]
car1 = Car(env, "car1", link)
car2 = Car(env, "car2", link)
env.run(until=15)