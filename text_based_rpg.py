from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, hero_class): 
        self.__health = 100
        self.__experience = 0
        self.name = name
        self.hero_class = hero_class
        self.weapon = None

    def attack(self):
        print(f"{self.name} attacks with power!")

    def take_damage(self, amount):
        self.__health -= amount
        print(f"{self.name} took {amount} damage.")
        if self.__health <= 0:
            print(f"{self.name} has been defeated.")

    def heal(self, amount):
        print(f"{self.name} healed for {amount} health.")
        self.__health = min(self.__health + amount, 100)

    def gain_xp(self, amount):
        self.__experience += amount

    @abstractmethod
    def ultimate_ability(self):
        pass

    def equip(self, weapon_obj):
        self.weapon = weapon_obj
        print(f"{self.name} equipped {weapon_obj}")

    def get_health(self):
        return self.__health

    def get_experience(self):
        return self.__experience 

    def display_stats(self):
        print(f"+---------- Hero Stats ----------+")
        print(f"Hero Name : {self.name}")
        print(f"Class : {self.hero_class}")
        print(f"Health : {self.__health} / 100")
        print(f"XP : {self.__experience}")

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, "Warrior")
        self.shield = 20

    def attack(self):
        print(f"{self.name} swings a mighty sword!")
        if self.weapon is not None:
           print(f"{self.name} attacks with {self.weapon}!")
           return self.weapon.damage + 15
        return 15

    def defend(self):
        print(f"{self.name} raises shield! Defense is now {self.shield}")

    def ultimate_ability(self):
        print(f"{self.name} goes BERSERK! Damage increases!")
        return 50

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, "Mage")
        self.mana = 50

    def attack(self):
        print(f"{self.name} casts a fireball!")
        if self.weapon is not None:
            print(f"{self.name} attacks with {self.weapon}!")
            return self.weapon.damage + 20
        return 20

    def cast_spell(self):
        self.mana -= 10
        print(f"{self.name} uses 10 mana to cast a spell! Mana left: {self.mana}")
    
    def ultimate_ability(self):
        print(f"{self.name} casts ARMAGEDDON! It rains fire!")
        return 70
    
class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f"{self.name}"
        
def battle_round(attacker, defender):
    damage = attacker.attack()
    defender.take_damage(damage)


def main():
    player1 = Warrior("KDA")
    player2 = Mage("LM")

    weapon1 = Weapon("Dragon Slayer", 50)

    player1.equip(weapon1)

    while True:
        print(f"+--------------------------------+")
        print(" 1. Attack")
        print(" 2. Use Ultimate")
        print(" 3. Heal")
        print(" 4. View Stats")
        print(" 5. Exit")
        print(f"+--------------------------------+")

        user_choice = input("Please enter a number : ")
        if user_choice == '1':
            battle_round(player1, player2)
            if player2.get_health() <= 0:
                print("You Win!")
                break 
            else:
                player1.take_damage(player2.attack())
        
        elif user_choice == '2':
            player1.ultimate_ability()
        
        elif user_choice == '3':
            player1.heal(10)

        elif user_choice == '4':
            player1.display_stats()

        elif user_choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()