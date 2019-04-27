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

    def getComputerTimeDelay(self):
        return self.getNtpTime() - datetime.datetime.now().timestamp()

    def now(self):
        return datetime.datetime.now().timestamp() + self.computerTimeDelay