class Weapon:
    def __init__(self, one_handed=True, strength=0, agility=0, intelligence=0, speed=0):
        self.one_h = one_handed
        self.st = strength
        self.ag = agility
        self.intel = intelligence
        self.sp = speed

    def is_one_handed(self):
        return self.one_h

    def strength(self):
        return self.st

    def agility(self):
        return self.ag

    def intelligence(self):
        return self.intel

    def speed(self):
        return self.sp

    def copy(self):

        return Weapon(self.one_h, self.st, self.ag, self.intel, self.sp)

    def __add__(self, other):
        return Weapon(one_handed=False, strength=self.st + other.st, agility=(self.ag + other.ag),
                      intelligence=(self.intel + other.intel), speed=(self.sp + other.sp))

    def __iadd__(self, other):
        self.one_h = False
        self.st += other.st
        self.ag += other.ag
        self.intel += other.intel
        self.sp += other.sp

    def __mul__(self, number):
        return Weapon(self.sp * number)

    def __imul__(self, number):
        self.sp *= number

    def __str__(self):
        if self.one_h:
            n = 1
        else:
            n = 2
        return f"Weapon[{n}](strength: {self.st}, agility: {self.ag}, intelligence: {self.intel}, speed: {self.sp})"


class Player:
    def __init__(self, strength=0, agility=0, intelligence=0, speed=0):
        self.st = strength
        self.ag = agility
        self.intel = intelligence
        self.sp = speed
        self.weapons = []

    def strength(self):
        return self.st

    def agility(self):
        return self.ag

    def intelligence(self):
        return self.intel

    def speed(self):
        if len(self.weapons) == 2:
            return (self.weapons[0].sp + self.weapons[1].sp) / 2
        elif len(self.weapons) == 1:
            return self.weapons[0].sp
        return 0

    def my_del(self):
        self.st -= self.weapons[0].st
        self.ag -= self.weapons[0].ag
        self.intel -= self.weapons[0].intel
        del self.weapons[0]
        self.sp = self.speed()

    def take_up_weapon(self, weapon):
        self.weapons.append(weapon.copy())
        if len(self.weapons) > 2:
            self.my_del()
        if len(self.weapons) == 2:
            if self.weapons[0].one_h == False or self.weapons[1].one_h == False:
                self.my_del()
        elif not self.weapons[0].one_h:
            self.my_del()

        self.st += weapon.st
        self.ag += weapon.ag
        self.intel += weapon.intel
        self.sp = self.speed()

    def throw_a_weapon(self):
        for i in range(len(self.weapons)):
            self.my_del()

    def __lshift__(self, weapon):
        self.take_up_weapon(weapon)

    def __neg__(self):
        self.throw_a_weapon()

    def __str__(self):
        return f"""Player[{len(self.weapons)}](
Strength: {self.st},
Agility: {self.ag},
Intelligence: {self.intel},
Speed: {self.speed()}
)
"""


weapon1 = Weapon(strength=3, speed=1)
weapon2 = Weapon(one_handed=False, agility=5, speed=3)
weapon3 = weapon1 * 2
weapon4 = weapon1 + weapon2
weapon5 = weapon4.copy()
print(weapon1)
print(weapon2)
print(weapon3)
print(weapon4)
print(weapon5)


