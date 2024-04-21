import threading
import time
from datetime import datetime

class Alarm(threading.Thread):
    """ A class which generates periodic alarms """
    
    def __init__(self, duration=1):
        self.duration = duration
        self.subscribers = []  
        self.flag = True
        threading.Thread.__init__(self, None, None)
    
    def register(self, subscriber):
        """ Register a subscriber for alarm notifications """
        self.subscribers.append(subscriber)
    
    def notify(self):
        """ Notify all the subscribers """
        for subscriber in self.subscribers:
            subscriber.update(self.duration)
    
    def stop(self):
        """ Stop the thread """
        self.flag = False
    
    def run(self):
        """ Run the alarm generator """
        while self.flag:
            time.sleep(self.duration)
            self.notify()  # Notify subscribers

class DumbClock(object):
    """ A dumb clock class using an Alarm object """
    
    def __init__(self):
        self.current = time.time()
    
    def update(self, *args):
        """ Callback method from publisher """
        self.current += args[0]
    
    def __str__(self):
        """ Display local time """
        return datetime.fromtimestamp(self.current).strftime('%H:%M:%S')
    

if __name__ == "__main__":
 alarm=Alarm(duration=1)
 clock=DumbClock()
 alarm.register(clock)
 print(clock);time.sleep(20);print(clock)