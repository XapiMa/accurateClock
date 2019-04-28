import requests
import json
import time
import datetime

class Clock:
    def __init__(self):
        self._computerTimeDelay = None
        self.setComputerTimeDelay()

    @property
    def computerTimeDelay(self):
        return self._computerTimeDelay
    
    @computerTimeDelay.setter
    def computerTimeDelay(self,computerTimeDelay):
        self._computerTimeDelay = computerTimeDelay

    def setComputerTimeDelay(self):
        self.computerTimeDelay = self.getComputerTimeDelay()

    def getNtpTime(self):
        url = "https://ntp-a1.nict.go.jp/cgi-bin/json"
        sendTime = datetime.datetime.now().timestamp()
        r = requests.get(url)
        arraiveTime = datetime.datetime.now().timestamp()
        latency = (arraiveTime - sendTime)/2
        data = json.loads(r.text)
        dataTime = data["st"]
        return dataTime - latency

    def getSingleComputerTimeDelay(self):
        return self.getNtpTime() - datetime.datetime.now().timestamp()

    def getComputerTimeDelay(self):
        delays = [self.getSingleComputerTimeDelay() for i in range(5)]
        delays.sort()
        return delays[2]

    def time(self):
        return int(self.monotonic())
    def monotonic(self):
        return datetime.datetime.now().timestamp() + self.computerTimeDelay
    def now(self):
        return datetime.datetime.fromtimestamp(self.time())