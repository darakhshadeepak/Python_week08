class Vehicle:
    def _init_(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
v=Vehicle()
v._init_(240,18)
print(v.max_speed ,v.mileage)
