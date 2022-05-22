"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def hello_user(x):
    while x != 'Хорошо':
        print('Как дела?')
        x = input()
    """
    Замените pass на ваш код
    """

    
if __name__ == "__main__":
    print('Как дела?')
    x = input()
    hello_user(x)
