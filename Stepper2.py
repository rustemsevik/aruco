import time

# only test for uln2003
class Stepper2:
    FULL_ROTATION = int(4075.7728395061727 / 8) # http://www.jangeox.be/2013/10/stepper-motor-28byj-48_25.html

    HALF_STEP = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
    ]

    FULL_STEP = [
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 1]
    ]
    def __init__(self, mode, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, delay):
    	if mode=='FULL_STEP':
        	self.mode = self.FULL_STEP
        else:
        	self.mode = self.HALF_STEP
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.pin5 = pin5
        self.pin6 = pin6
        self.pin7 = pin7
        self.pin8 = pin8
        self.delay = delay  # Recommend 10+ for FULL_STEP, 1 is OK for HALF_STEP
        
        # Initialize all to 0
        self.reset()
        
    def step(self, count, direction=1):
        """Rotate count steps. direction = -1 means backwards"""
        if count<0:
            direction = -1
            count = -count
        for x in range(count):
            for bit in self.mode[::direction]:
                self.pin1(bit[0])
                self.pin2(bit[1])
                self.pin3(bit[2])
                self.pin4(bit[3])
                time.sleep_ms(self.delay)
        self.reset()
    
    def double(self, count, direction=1):
        """Rotate count steps. direction = -1 means backwards"""
        if count<0:
            direction = -1
            count = -count
        for x in range(count):
            for bit in self.mode[::direction]:
                self.pin1(bit[0])
                self.pin5(bit[0])
                self.pin2(bit[1])
                self.pin6(bit[1])
                self.pin3(bit[2])
                self.pin7(bit[2])
                self.pin4(bit[3])
                self.pin8(bit[3])
                time.sleep_ms(self.delay)
        
        
    def angle(self, r, direction=1):
    	self.step(int(self.FULL_ROTATION * r / 360), direction)
    def reset(self):
        # Reset to 0, no holding, these are geared, you can't move them
        self.pin1(0) 
        self.pin2(0) 
        self.pin3(0) 
        self.pin4(0)

def create(pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, delay=2, mode='HALF_STEP'):
	return Stepper2(mode, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8, delay)


