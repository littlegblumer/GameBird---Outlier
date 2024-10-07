class GameBird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} is flying")

# Creating an instance of Gamebird
bird = GameBird("Sparrow")
bird.fly()