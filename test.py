import simpy

def car(env):
    while True:
        print("parrk %d" % env.now)
        park_duration = 5
        yield env.timeout(park_duration)

        print("star driving %d" % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)

env = simpy.Environment()
env.process(car(env))
env.run(until=20)