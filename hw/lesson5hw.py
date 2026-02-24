import functools


def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана с аргументами {args}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        print("Функция завершена")
        
        return result
    
    return wrapper

@log_execution
def add(a, b):
    return a + b

@log_execution
def multiply(x, y):
    return x * y

@log_execution
def greet(name):
    return f"Hello, {name}!"

@log_execution
def power(base, exponent):
    return base ** exponent


if __name__ == "__main__":
    print("=== Тестирование декоратора log_execution ===\n")
    
    print("Тест 1:")
    result1 = add(5, 3)
    print(f"Возвращенное значение: {result1}\n")
    
   
    print("Тест 2:")
    result2 = multiply(4, 7)
    print(f"Возвращенное значение: {result2}\n")
    
    print("Тест 3:")
    result3 = greet("Ardager")
    print(f"Возвращенное значение: {result3}\n")
    
    print("Тест 4:")
    result4 = power(2, 10)
    print(f"Возвращенное значение: {result4}\n")


class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def __str__(self):
        return f"User(name='{self.name}', role='{self.role}')"


def require_admin(func):
    def wrapper(user, *args, **kwargs):
        if hasattr(user, 'role') and user.role == 'admin':
            return func(user, *args, **kwargs)
        else:
            print("Доступ запрещён")
            return None
    
    return wrapper



@require_admin
def delete_database(user):
    print("База данных удалена")

@require_admin
def create_user(user, new_user_name):
    print(f"Пользователь {new_user_name} создан")

@require_admin
def view_logs(user):
    print("Содержимое логов:")
    print("- 2024-01-01: System started")
    print("- 2024-01-02: User login")
    print("- 2024-01-03: Database backup")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("=== Тестирование декоратора require_admin ===")
    print("="*50 + "\n")

    admin_user = User("Admin", "admin")
    regular_user = User("RegularUser", "user")
    
    print(f"Администратор: {admin_user}")
    print(f"Обычный пользователь: {regular_user}\n")
    
    print("Тест 1: Администратор удаляет базу данных")
    delete_database(admin_user)
    print()
   
    print("Тест 2: Обычный пользователь пытается удалить базу данных")
    delete_database(regular_user)
    print()
    
    print("Тест 3: Администратор создает пользователя")
    create_user(admin_user, "NewUser")
    print()
 
    print("Тест 4: Обычный пользователь пытается создать пользователя")
    create_user(regular_user, "NewUser")
    print()
    
    print("Тест 5: Администратор просматривает логи")
    view_logs(admin_user)
    print()
    
    print("Тест 6: Обычный пользователь пытается просмотреть логи")
    view_logs(regular_user)
    print()
