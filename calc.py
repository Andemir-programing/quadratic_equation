# -*- coding: utf-8 -*-
"""calc.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16yp51a4BFyEIHJEyzmNRSgJ7JQH90Gp1
"""

#подсказки

INFO = '''   \nДля решения квадратного уравнения
вида: a*x**2 + b*x + c = 0
введите последовательно значения
a, b, c, каждый раз нажимая Enter:\n'''

HELP = '''   \nВведено не верное значение,
введите "y" чтобы решить ещё одно
уравнение, или "n" чтобы выйти: '''

ERROR = ''' \nЭто не квадратное уравнение.
Коэффициент а не может быть равен нулю.
Введите верные значения.\n'''

EXIT = '''  \nСпасибо, что выбрали наше приложение.
До новых встреч! (❁´◡`❁)'''

UPS = '''   \nУпссс... (⊙_⊙;)
  Похоже Вы ошиблись и ввели не
числовые значения коэффициентов.
Попробуйте ещё раз, 
и будьте внимательны!\n'''

#переменная-выключатель
run = True
while run:
    #информационная подсказка
    print(INFO)
    try:
    #запрашиваем у пользователя значения коэффициентов уравнения
      a = float(input("Введите значение a: "))
      b = float(input("Введите значение b: "))
      c = float(input("Введите значение c: "))

    #в случае ошибки печатаем подсказку
    except ValueError:
        print(UPS)
      
    else: 
        #обрабатываем нулевое значение коэффициента при x^2 
        if a == 0:
            print(ERROR)
            run = True

        
        else:
            # вычисляем дискриминант
            D = b ** 2 - 4 * a * c  
            print("\nДискриминант = ", round(D, 2))

            #находим корни уравнения
            if D > 0:
                X1 = (-b - D ** 0.5) / (2 * a)
                X2 = (-b + D ** 0.5) / (2 * a)
                print("X1 =", round(X1, 2), "X2 =", round(X2, 2))

            elif D == 0:
                X = (-b / 2 * a)
                print("X =", round(X, 2))

            else:
                print('Дискриминант меньше 0, корней нет.\n¯\\_(ツ)_/¯')

            question = input('\nХотите решить ещё одно уравнение? y/n: ').lower()
            
            #перменная-выключатель
            y_n = True
            

            while y_n:
                #нужно решить еще одно уравнение
                if question == 'y':
                    run = True
                    y_n = False

                #выходим из программы
                elif question == 'n':
                    print(EXIT)
                    run = False
                    y_n = False

                #подсказка-помощь
                else:
                    question = input(HELP).lower()
                    y_n = True
                    run = False



