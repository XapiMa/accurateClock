# accurateClock
hows more accurate time than the computer's internal clock.

If you are not using ntp, your computer's internal time may be incorrect.
This tool shows more accurate time than the computer's internal clock.
It calculates the built-in clock delay based on the NTP information provided by NICT and provides more accurate UNIX time.

## installation
 ```
 $ pip install git+ssh://git@github.com/XapiMa/accurateClock.git
 ```

 or 

  ```
 $ pip install git+https://github.com/XapiMa/accurateClock.git
 ```

## usage

```python
from accurateClock import Clock

clock = Clock()

# get int unix time
print("clock.time():{}".format(clock.time()))

# get float unix time
print("clock.monotonic():{}".format(clock.monotonic()))

# get datetime.datetime
print("clock.now():{}".format(clock.now()))

# get computer's internal delay
print("clock.computerTimeDelay:{}".format(clock.computerTimeDelay))
```


If the amount of delay may have changed, you can reset the computer's internal time delay.
```python
from accurateClock import Clock

clock = Clock()
clock.setComputerTimeDelay()

print(clock.now())
```


If you want to know the computer's internal time delay, you can do it as follows.
```python
from accurateClock import Clock

clock = Clock()
print(clock.computerTimeDelay)
```
