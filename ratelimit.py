#!/usr/bin/python

import datetime

class RateLimit():
    def __init__(self, limit, period):
        self.hits = []
        self.limit = limit
        self.period = period

    def __thin(self):
        now = datetime.datetime.now()
        for i,val in enumerate(self.hits):
            if now - val > self.period:
                self.hits.pop(i)

    def hit(self):
        self.__thin()
        if len(self.hits) < self.limit:
            self.hits.append(datetime.datetime.now())
            return True
        else:
            return False
    def remain(self):
        self.__thin()
        return self.period - (datetime.datetime.now() - self.hits[0])


def main():
    import time

    rl = RateLimit(1, datetime.timedelta(seconds=3))
    print(f"Test for ratelimit: {rl.limit}/{rl.period.total_seconds()}s")
    for i in range(1,11):
       t=datetime.datetime.now().strftime("%F %T")
       print(f"[{t}] attempt #{i}: {rl.hit()} ({rl.remain().total_seconds()}s remain)")
       time.sleep(1)


if __name__ == "__main__":
    main()
    
