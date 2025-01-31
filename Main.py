import random

print('Приветствую тебя в SmartKit!')
print('SmartKit - простой помощник!')
print('Давайте начнём работу!')

nick = input('Введите ваше имя: ')
print(nick, 'Отличное имя')

key = 'd-d-1'
print('Чтобы начать работу SmartKit активируйте её!')
key_answer = input('Введите ключ: ')

if key == key_answer:
    print('Отлично! Лицензия активирована!')
    print('Подождите немного....')
    print('Подключение к службам Steelfox Games')

    def generator_password(length=12):
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        numbers = '0123456789'
        plus = letters + numbers

        password = ''.join(random.choices(plus, k=length))
        return password

    def calculator():
        print("Добро пожаловать в калькулятор!")
        print("Вы можете выполнять операции: +, -, *, /")
        while True:
            num1 = input("Введите первое число: ")
            if not num1.replace('.', '', 1).isdigit():
                print("Ошибка: введите корректное число!")
                continue

            operation = input("Введите операцию (+, -, *, /): ")
            if operation not in ["+", "-", "*", "/"]:
                print("Некорректная операция! Попробуйте снова.")
                continue

            num2 = input("Введите второе число: ")
            if not num2.replace('.', '', 1).isdigit():
                print("Ошибка: введите корректное число!")
                continue

            num1 = float(num1)
            num2 = float(num2)

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                    continue
                result = num1 / num2

            print("Результат:", result)

            again = input("Хотите выполнить ещё одну операцию? (да/нет): ")
            if again.lower() != "да":
                break

    def main():
        while True:
            print("1 - Калькулятор")
            print("2 - Придумать сложный пароль")
            print("0 - Выйти")
            answer = input('Чем тебе помочь: ')

            if answer == "1":
                calculator()
            elif answer == "2":
                length = input("Введите длину пароля: ")
                if not length.isdigit() or int(length) <= 0:
                    print("Ошибка: введите корректное число для длины!")
                    continue
                print("Ваш сгенерированный пароль:", generator_password(int(length)))
            elif answer == "0":
                print('Хорошо, удачи!')
                break
            else:
                print("Некорректный ввод. Повторите попытку.")

    main()
else:
    print('К сожалению, у вас нет лицензии')
