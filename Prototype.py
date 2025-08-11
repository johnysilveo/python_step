import copy



class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color

    def clone(self):
        return copy.copy(self)

proto_car = Car("Lexus", 'Orange')
cloned_car = proto_car.clone()

print('original: ', vars(proto_car))
print('copy: ', vars(cloned_car))