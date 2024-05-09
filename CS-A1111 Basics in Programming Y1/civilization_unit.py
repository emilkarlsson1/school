import random


class CivilizationUnit:
    MAX_HP = 100
    DAMAGE_SCALE = 30
    RANDOM_DAMAGE_DIFF = 8

    def __init__(self, unit_name, attack, defense=None, is_ranged=False):
        "Initializes a new CivilizationUnit"
        self.__name = unit_name
        self.__attack_strength = attack
        if defense is not None:
            self.__defense_strength = defense
        else:
            self.__defense_strength = attack
        self.__fortified = False
        self.__ranged = is_ranged
        self.__hp = CivilizationUnit.MAX_HP

    def get_name(self):
        return self.__name

    def is_alive(self):
        return not self.is_eliminated()

    def is_eliminated(self):
        if self.__hp == 0:
            return True
        else:
            return False

    def get_effective_defense_strength(self):
        h = self.__hp * 0.50
        h2 = h + 50
        htot = h2 / 100
        if self.__fortified:
            lasku = 1.4 * htot * self.__defense_strength
            return lasku
        else:
            lasku = htot * self.__defense_strength
            return lasku

    def get_effective_attack_strength(self):
        h = self.__hp * 0.50
        h2 = h + 50
        htot = h2 / 100
        lasku = htot * self.__attack_strength
        return lasku

    def attack(self, other_unit):
        h = other_unit.defend(self)
        if self.__ranged:
            damage_taken = 0
            return h, damage_taken
        else:
            damage_taken = self.defend(other_unit)
            return h, damage_taken

    def defend(self, other_unit):
        excepted_damage_taken = int(CivilizationUnit.DAMAGE_SCALE *
                                    other_unit.get_effective_attack_strength() / self.get_effective_defense_strength())
        max_diff = CivilizationUnit.RANDOM_DAMAGE_DIFF
        actual_damage_taken = max(1, random.randint(excepted_damage_taken
                                                    - max_diff, excepted_damage_taken + max_diff))

        damage_taken = self.__hp - actual_damage_taken
        if damage_taken >= 0:
            self.__hp = damage_taken
        else:
            self.__hp = 0
        return actual_damage_taken

    def fortify(self):
        self.__fortified = True

    def unfortify(self):
        self.__fortified = False

    def heal(self, amount):
        tot = self.__hp + amount
        if tot <= 100:
            self.__hp += amount
        else:
            self.__hp = CivilizationUnit.MAX_HP
        return self.__hp

    def get_hp(self):
        return self.__hp

    def is_fortified(self):
        return self.__fortified

    def __str__(self):
        if self.__ranged:
            if self.__hp > 0:
                if self.__fortified:
                    return "{:s} - {:d}/{:d} (ranged) - HP: {:d}, FORTIFIED".format(self.__name, self.__attack_strength,
                                                                                    self.__defense_strength, self.__hp)
                else:
                    return "{:s} - {:d}/{:d} (ranged) - HP: {:d}".format(self.__name, self.__attack_strength,
                                                                         self.__defense_strength, self.__hp)
            else:
                return "{:s} - {:d}/{:d} (ranged) - HP: {:d}, ELIMINATED".format(self.__name, self.__attack_strength,
                                                                                 self.__defense_strength, self.__hp)
        else:
            if self.__hp > 0:
                if self.__fortified:
                    return "{:s} - {:d}/{:d} (melee) - HP: {:d}, FORTIFIED".format(self.__name, self.__attack_strength,
                                                                                   self.__defense_strength, self.__hp)
                else:
                    return "{:s} - {:d}/{:d} (melee) - HP: {:d}".format(self.__name, self.__attack_strength,
                                                                        self.__defense_strength, self.__hp)
            else:
                return "{:s} - {:d}/{:d} (melee) - HP: {:d}, ELIMINATED".format(self.__name, self.__attack_strength,
                                                                                self.__defense_strength, self.__hp)
