import abc
class Biddable(abc.ABC):
    @abc.abstractmethod
    def hours_remaining(self):
        pass
    @abc.abstractmethod
    def worked_perc(self):
        pass
    @abc.abstractmethod
    def overbid(self):
        pass
    
    
class Shot(Biddable):

    def __init__(self,bid,worked = 0):
        self._bid = bid
        self._worked = worked

    def add_hours(self,hours):
        self._worked += hours

    def set_bid(self,hours):
        self._bid = hours

    def hours_remaining(self):
        return self._bid - self._worked
    
    def worked_perc(self):
        return (self._worked/self._bid)*100
    
    def overbid(self):
        return self._worked > self._bid
    
    def worked(self):
        return self._worked
    
    def bid(self):
        return self._bid
    
class Sequence(Biddable):
    def __init__(self):
        self._shots:list[Shot] = []

    def add_shot(self,shot:Shot):
        self._shots.append(shot)
    
    def remove_shot(self,shot:Shot):
        if shot in self._shots:
            index = self._shots.index(shot)
            self._shots.pop(index)

    def worked_perc(self):
        # return 
        hours_bid = 0
        hours_worked = 0
        for i in self._shots:
            hours_bid+=i.bid
            hours_worked+=i.worked
        return (hours_worked/hours_bid)*100
    
    def hours_remaining(self):
        # return to total hours remaining
        remaining_hours = 0
        for i in self._shots:
            remaining_hours+=i.hours_remaining()
        return remaining_hours
        
    def overbid(self):
        hours_bid = 0
        hours_worked = 0
        for i in self._shots:
            hours_bid+=i.bid()
            hours_worked += i.worked()
        return hours_worked > hours_bid

# test
shot1 = Shot(12,2)
shot2 = Shot(2,3)

assert shot1.overbid() == False,"overbid not working correctly in shot1"
assert shot2.overbid() == True,"overbid not working correctly in shot2"

assert shot1.hours_remaining() == 10,f"incorrect hours remianing expected 10 received {shot1.hours_remaining()}"
assert shot2.hours_remaining() == -1,f"incorrect hours remianing expected -1 received {shot1.hours_remaining()}"

bigsequence = Sequence()
bigsequence.add_shot(shot1)
bigsequence.add_shot(shot2)

assert bigsequence.hours_remaining() == 9,f"incorrect hours remaining expected 9, received {bigsequence.hours_remaining()} "
assert bigsequence.overbid() == False,f"incoorect overbid, expected false received True"

bigsequence.remove_shot(shot1)
assert bigsequence.overbid() == True,f"shot1 not removed {bigsequence._shots[0]}"