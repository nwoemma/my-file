class livingthings:
    def live(self):
        pass

class humanbeings(livingthings):
    def lives(others):
        pass


obj_livingthings = livingthings()
obj_humanbeings = humanbeings()

print(type(obj_humanbeings) == humanbeings)
print(type(obj_humanbeings) == livingthings) 

print(isinstance(obj_livingthings,livingthings))
print(isinstance(obj_humanbeings,livingthings))