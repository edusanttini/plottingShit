import numpy as np
from sympy import *
import matplotlib.pyplot as plt
x, y, z = symbols('x y z')


def get_user_entry(degree):
    return input("Digite o coeficiente do termo de grau ", degree)


def get_user_info(degree):
    first = input("Digite o coeficiente do termo de grau 2: ")
    sec = input("Digite o coeficiente do termo de grau 1: ")
    third = input("Digite o coeficiente do termo de grau 0: ")
    try:
        int(first); int(sec); int(third);
        is_int = true
    except ValueError:
        is_int = false
    print(is_int)
    if is_int:
        eq = int(first) * (x ** 2) + int(sec) * x + int(third)
    else:
        if first.isnumeric() and not sec.isnumeric() and third.isnumeric():
            print("get_user_info01", first.isnumeric())
            print("get_user_info02", sec.isnumeric())
            print("get_user_info03", third.isnumeric())
            eq = ""+first + "* (x ** 2)" + "+" + ""+sec + "+" + ""+third
        elif sec.isnumeric() and not first.isnumeric() and third.isnumeric():
            print("get_user_info3")
            eq = ""+first + "+" + ""+sec + "*x" + "+" + ""+third
        elif first.isnumeric() and sec.isnumeric():
            print("get_user_info4")
            eq = ""+first + "* (x ** 2)" + "+" + ""+sec + "*x" + "+" + ""+third
        else:
            print("else")
            eq = ""+first + "+" + ""+sec + "+" + ""+third
    return first, sec, third, eq


def get_user_higher_degree_eq_info(degree):
    a = input("Digite o coeficiente do termo de grau" + str(degree))
    b = ""
    c = ""
    if degree == 3:
        eq = a*(x**3)
    elif degree >= 4:
        b = input("Digite o coeficiente do termo de grau " + str(degree - 1))
        eq = a*(x**4) + b*(x**3)
    elif degree > 4:
        c = input("Digite o coeficiente do termo de grau " + str(degree - 2))
        eq = a*(x**5) + b*(x**4) + c*(x**3)
    return eq


def create_equation(degree):
    if degree == 2:
        eq = get_user_info(2)
    elif degree == 3:
        eq_higher = get_user_higher_degree_eq_info(3)
        eq = get_user_info(2)
        eq = eq_higher + eq
    elif degree == 4:
        eq_higher = get_user_higher_degree_eq_info(4)
        eq = get_user_info(2)
        eq = eq_higher + eq
    return eq


def get_eq_degree():
    degree = int(input("Digite o grau da equação selecionada"))
    if degree == 1:
        print("Por favor, escolha uma equação de no mínimo segundo grau")
    elif degree == 2:
        eq = create_equation(2)
    elif degree == 3:
        eq = create_equation(3)
    elif degree == 4:
        eq = create_equation(4)
    elif degree == 5:
        eq = create_equation(5)
    return eq


def get_eq_abs_value(eq, var_to_change, new_var, is_plot):
    eq = str(eq)
    char={var_to_change:str(new_var)}
    string=list(eq)
    for index,item in enumerate(string):
        for key,value in char.items():
            if item==key:
                string[index]=value
    str_eq = "".join(string)
    if is_plot:
        return str_eq
    int_eq = eval(str_eq)
    return int_eq


def plotar(a, b, c, x, eq):
    x = np.linspace(x - 5, x + 5, 20)
    eq = get_eq_abs_value(eq, "a", a, true)
    eq = get_eq_abs_value(eq, "b", b, true)
    eq = get_eq_abs_value(eq, "c", c, true)
    y = eval(eq)
    plt.plot(x, y)  # gráfico de linha
    plt.plot(x, y, 'o')  # gráfico com pontos
    plt.axvline(x=0, c="black", label="x=0")
    plt.axhline(y=0, c="black", label="y=0")
    plt.show()  # mostra o gráfico
