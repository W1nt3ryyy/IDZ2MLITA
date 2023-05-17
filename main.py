def start():
    print("Введите скобочную последовательность:")
    input_str = input()
    input_str += '#'
    i = 0
    symbol = 'a'
    return input_str, symbol, i

letters='abcdefghijklmnopqrstuvwxyz'


class ParseError(Exception):
    def __init__(self):
        print('error')


def error():
    raise ParseError()


def read():
    global symbol, i
    i += 1
    symbol = input_str[i]


class MainClass():

    # Формула
    def formula(self):
        self.expression()
        if (symbol == '#'):
            return
        error()

    # Выражение
    def expression(self):

        if (symbol == '('):
            self.expression_round0()
        elif (symbol == '['):
            self.expression_square0()
        elif self.letter():
            self.alphabet0()


    def expressioninner(self):

        if (symbol == '('):
            self.expression_round0()
        elif (symbol == '['):
            self.expression_square0()
        elif self.letter():
            self.alphabetinner()
        else:
            error()

    def alphabet0(self):
        read()
        self.alphabet1()


    def alphabetinner(self):
        read()
        self.alphabet2()

    def alphabet1(self):

        if (symbol == '+') or (symbol == '-') or (symbol == '/'):
            self.signs()
            self.expression()
        elif (symbol == '(') or (symbol == '[') or (self.letter()):
            self.expression()

    def alphabet2(self):

        if (symbol == '+') or (symbol == '-') or (symbol == '/'):
            self.signs()
            self.expression()
        elif (symbol == '(') or (symbol == '[') or (self.letter()):
            self.expression()
        else:
            error()

    # Выражение в круглых скобках
    def expression_round0(self):

        if (symbol == '('):
            read()
            self.expressioninner()
            if (symbol == ')'):
                read()
            else:
                print('Скобка не закрыта')
                error()
            self.expression_round1()

    def expression_round1(self):

        if (symbol == '+') or (symbol == '-') or (symbol == '/'):

            self.signs()

            self.expression_round2()
        elif (symbol == '[') or (self.letter()):

            self.expression_round2()

    def expression_round2(self):

        if (symbol == '['):

            self.expression_square0()
        elif (self.letter()):
            self.alphabet0()
        else:
            error()

    def expression_square0(self):

        if (symbol == '['):
            read()
            self.expressioninner()
            if (symbol == ']'):
                read()
            else:
                print("Скобка не закрыта")
                error()
            self.expression_square1()

    def expression_square1(self):

        if (symbol == '+') or (symbol == '-') or (symbol == '/'):

            self.signs()

            self.expression_square2()
        elif (symbol == '(') or (self.letter()):

            self.expression_square2()

    def expression_square2(self):

        if (symbol == '('):

            self.expression_round0()
        elif (self.letter()):
            self.alphabet0()
        else:
            error()

    # Знаки
    def signs(self):
        read()


    def letter(self):
        if symbol in letters:
            return 1
        else:
            return 0


def main():
    global symbol
    symbol = input_str[0]
    m = MainClass()
    try:
        m.formula()
    except ParseError:
        print('false')
        return
    print('true')


print("Условие задания:")
print(" Правильная скобочная запись арифметических выражений с двумя видами скобок. ", " \n",
      "После круглой скобки всегда должна стоять квадратная, после квадратной - круглая. ", " \n",
      "Знак умножения не пишется и обозначается отсутствием знака. ", " \n",
      "Могут быть “лишние” скобки, но одна буква не может браться в скобки.\n")
print("Правильная запись: [ab((d+cd)[[a-b]])]/((a+b-c)[(c+d)])")
print("Неправильная запись [(a*c+b)([c-(d)]/([a+b-c](b-c)(d/e)))]\n")
print("В программе можно ввести с клавиатуры, можно выбрать из предложенных")
print("Для ввода с клавиатуры используется английская раскладка "
      "два вида скобок (), [], символы /, +, -.")
print("\n")

print("Если хотите продолжить нажмите Enter")
print("Если хотите выйти введите 0")
a2 = input()
while a2 != '0':
    input_str, symbol, i = start()
    main()
    print("Если хотите продолжить нажмите Enter")
    print("Если хотите выйти введите 0")
    a2 = input()
print("До свидания!")
