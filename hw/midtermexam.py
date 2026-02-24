#1. Создать базовый класс Hero
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    
    def action(self):
        return f"{self.name} готов к бою!"

#2. Создать два дочерних класса
class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    
    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"

class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"

#3. Создать класс BankAccount
class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name
    
    def login(self, password):
        return password == self.__password
    
    def full_info(self):
        return f"Герой: {self.hero.name}, Баланс: {self._balance} SOM"
    
    def get_bank_name(self):
        return self.bank_name
    
    def bonus_for_level(self):
        return self.hero.lvl * 10
    
    #4. Реализовать магические методы
    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"
    
    def __add__(self, other):
        if not isinstance(other, BankAccount):
            raise TypeError("Можно складывать только счета")
        
        # Проверяем, что герои одного класса
        hero1_class = type(self.hero).__name__
        hero2_class = type(other.hero).__name__
        
        if hero1_class != hero2_class:
            raise ValueError("Складывать счета можно только для героев одного класса")
        
        # Возвращаем сумму балансов
        return self._balance + other._balance
    
    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return False
        
        return (self.hero.name == other.hero.name and 
                self.hero.lvl == other.hero.lvl)
from abc import ABC, abstractmethod
#5. Абстрактный класс SmsService
class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass

class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"

class RUSms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": phone}

# Пример использования
if __name__ == "__main__":
    mage1 = MageHero("Merlin", 80, 500, 150)
    mage2 = MageHero("Merlin", 80, 500, 200)
    warrior = WarriorHero("Conan", 50, 900, 20)
    acc1 = BankAccount(mage1, 5000, "1234", "Simba")
    acc2 = BankAccount(mage2, 3000, "0000", "Simba")
    acc3 = BankAccount(warrior, 2500, "1111", "Simba")

    print(mage1.action())
    print(warrior.action())
    print(acc1)
    print(acc2)
    
    # --- Классовые и статические методы ---
    print("Банк:", acc1.get_bank_name())
    print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

    # --- Магические методы: __add__ ---
    try:
        print("Сумма счетов двух магов:", acc1 + acc2)
    except (ValueError, TypeError) as e:
        print("Нельзя сложить счета героев разных классов!", e)

    try:
        print("Сумма мага и воина:", acc1 + acc3)
    except (ValueError, TypeError) as e:
        print("Ошибка при сложении мага и воина:", e)

    # --- Магический метод: __eq__ ---
    print("Mage1 == Mage2 ?", acc1 == acc2)  # True — одинаковое имя и уровень
    print("Mage1 == Warrior ?", acc1 == acc3)  # False

    # --- SMS ---
    sms = KGSms()
    print("\n", sms.send_otp("+996777123456"))

# Декоратор log_execution
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана с аргументами {args}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        print("Функция завершена")
        return result
    return wrapper

# Пример использования
@log_execution
def add(a, b):
    return a + b

# Тестирование декоратора
print("\n--- Тестирование декоратора log_execution ---")
add(5, 3)