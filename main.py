from accurateClock import Clock

clock = Clock()
print("now:{}".format(clock.now()))
clock.setComputerTimeDelay()
print("set now delay")
print("now:{}".format(clock.now()))
print("delay:{}".format(clock.computerTimeDelay))

