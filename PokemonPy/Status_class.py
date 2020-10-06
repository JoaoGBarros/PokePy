class Status:

    def __init__(self, hp, ataque, defense, sp_attack, sp_defense, speed):
        self.hp = hp
        self.max = hp
        self.ataque = ataque
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed

    def get_stats(self):
        lista = {
            "Hp": self.hp,
            "Ataque": self.ataque,
            "Defese": self.defense,
            "Sp.Attack": self.sp_attack,
            "Sp.Defense": self.sp_defense,
            "Speed": self.speed
        }
        return lista

    def get_hp(self):
        return self.hp

    def get_attack(self):
        return self.ataque

    def get_defense(self):
        return self.defense

    def get_sp_attack(self):
        return self.sp_attack

    def get_sp_defense(self):
        return self.sp_defense

    def get_speed(self):
        return self.speed