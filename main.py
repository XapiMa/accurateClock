from accurateClock import Clock

clock = Clock()
print("clock.time():{}".format(clock.time()))
print("clock.monotonic():{}".format(clock.monotonic()))
print("clock.now():{}".format(clock.now()))
print("clock.computerTimeDelay:{}".format(clock.computerTimeDelay))

clock.setComputerTimeDelay()

