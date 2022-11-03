import datetime
# from datetime import datetime

class TimeKeeper:
    TimeInMinutes = 0
    endTime = None

    def __init__(self, min):
        self.TimeInMinutes = min
        self.endTime = datetime.datetime.now() + datetime.timedelta(minutes=min)

    def hasPassed(self):
        return datetime.datetime.now() > self.endTime