import simpy

class Car(object):
    def __init__(self, env, name) -> None:
        super().__init__()
        self.env = env
        self.action = env.process(self.run())
        self.name = name

    def run(self):
        while True:
            print(self.name, "parrk %d" % self.env.now)
            charge_duration = 5
            yield self.env.process(self.charge(charge_duration))

            print(self.name, "star driving %d" % self.env.now)
            trip_duration = 2
            yield self.env.timeout(trip_duration)
    
    def charge(self, duration):
        yield self.env.timeout(duration)

env = simpy.Environment()
car1 = Car(env, "car1")
car2 = Car(env, "car2")
env.run(until=15)