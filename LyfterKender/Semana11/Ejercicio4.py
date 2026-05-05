class Head:
    def __init__(self):
        self.brain = "Cerebro activo"

class Hand:
    def __init__(self, side):
        self.side = side  # "left" o "right"

class Arm:
    def __init__(self, side, hand):
        self.side = side
        self.hand = hand

class Feet:
    def __init__(self, side):
        self.side = side

class Leg:
    def __init__(self, side, foot):
        self.side = side
        self.foot = foot

class Torso:
    def __init__(self, head, left_arm, right_arm, left_leg, right_leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg


class Human:
    def __init__(self):
        self.head = Head()
        self.left_arm = Arm("left", Hand("left"))
        self.right_arm = Arm("right", Hand("right"))
        self.left_leg = Leg("left", Feet("left"))
        self.right_leg = Leg("right", Feet("right"))
        self.torso = Torso(self.head, self.left_arm, self.right_arm, self.left_leg, self.right_leg)

    def __str__(self):
        return (f"Human with {self.head.brain}, "
                f"{self.left_arm.side} arm with {self.left_arm.hand.side} hand, "
                f"{self.right_arm.side} arm with {self.right_arm.hand.side} hand, "
                f"{self.left_leg.side} leg with {self.left_leg.foot.side} foot, "
                f"{self.right_leg.side} leg with {self.right_leg.foot.side} foot.")
    

    #Las clases son el template de humanos, y los objetos son las instancias de esas clases.

head = Head()
left_arm = Arm("left", Hand("left"))
right_arm = Arm("right", Hand("right"))           
left_leg = Leg("left", Feet("left"))
right_leg = Leg("right", Feet("right"))
torso = Torso(head, left_arm, right_arm, left_leg, right_leg)
human = Human()
print(human)  # Imprime la descripcion del humano
print(human.torso.head.brain)  # Accede al cerebro del humano