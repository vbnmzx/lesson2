"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def hello_user(x):
	while x != 'Хорошо':
		try:
			x = input('Как дела?: ')
		except:
			print('Пока')
			break


if __name__ == "__main__":
	x = input('Как дела?: ')
	hello_user(x)
