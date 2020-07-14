Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.

---------------------------Math---------------------------

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle = abs(hour%12*30 + minutes*0.5 - minutes*6)
        return min(angle, 360-angle)
