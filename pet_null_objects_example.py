class Human:
    def express_affection_towards(self, pet):
        if pet:
            pet.feed()
            pet.stroke()


class Dog:
    def __init__(self):
        self.isHappy = False

    def feed(self):
        self.isHappy = True

    def stroke(self):
        self.isHappy = True
