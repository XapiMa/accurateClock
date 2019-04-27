# accurateClock
hows more accurate time than the computer's internal clock

This tool shows more accurate time than the computer's internal clock.

This tool calculates the built-in clock delay based on the NTP information provided by NICT and provides more accurate UNIX time.

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

print(clock.now())
```


If there is a risk that the computer's internal time delay has changed, you can reset the computer's internal time delay.
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
