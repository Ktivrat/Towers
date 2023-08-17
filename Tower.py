import random

# Определяем базовый класс башни
class Tower:
    def __init__(self, name, health, armor):
        self.name = name
        self.health = health
        self.armor = armor
        
    def increase_health(self, amount):
        self.health += amount
        
    def decrease_health(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        
    def increase_armor(self, amount):
        self.armor += amount
        
    def decrease_armor(self, amount):
        self.armor -= amount
        if self.armor < 0:
            self.armor = 0
            
            
        
# Определяем подкласс стрелковой башни, наследующий функциональность от класса Tower
class ArcherTower(Tower):
    def __init__(self, name, health, armor, min_damage, max_damage):
        super().__init__(name, health, armor)
        self.damage = min_damage
        self.damage = max_damage
        
    def shoot(self, target):
        if self.health > 0:
            if self.armor > 0:
                effective_damage = self.damage - self.armor
                if effective_damage > 0:
                    target.decrease_health(effective_damage)
            else:
                target.decrease_health(self.damage)
    
    
    
# Создаем две стрелковые башни
tower1 = ArcherTower("Tower 1", 110, 15, 12, 25)
tower2 = ArcherTower("Tower 2", 110, 15, 12, 25)


# Сражение
while tower1.health > 0 and tower2.health > 0:
    attacker = random.choice([tower1, tower2])
    target = tower1 if attacker == tower2 else tower2
    attacker.shoot(target)
    print(f"{attacker.name} shoots {target.name}.\n {target.name} health: {target.health}")
    
    
    
# Определение победителя
if tower1.health <= 0 and tower2.health <= 0:
    print("It's a draw!")
elif tower1.health <= 0:
    print(f"{tower2.name} wins!")
else:
    print(f"{tower1.name} wins!")



