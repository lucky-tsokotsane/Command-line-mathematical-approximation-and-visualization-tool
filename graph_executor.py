import matplotlib.pyplot as plt
import sympy as sp

x = sp.symbols('x')
f_eq = x**(1/2)
deriv_f = sp.diff(f_eq)

def tabular_point(function_equation, problem_point):
    known_point = []

    for i in range(0, problem_point + 1):
        function_result = function_equation.subs(x, i)

        if (function_result % 1) == 0:
            known_point.append(i)
        else:
            continue

    known_point.sort(reverse=True)
    return known_point[0]


def taylor_polynomial_function(problem_point, polynomial_order):
    a0 = f_eq.subs(x, problem_point)
    derived_function = deriv_f

    for i in range(0, polynomial_order + 1):
        a0 = a0 + (derived_function.subs(x, problem_point) / sp.factorial(i)) * (problem_point - tabular_point(f_eq, problem_point)) ** i
        derived_function = sp.diff(derived_function)

    return a0


def linear_value_approximator(problem_point):
    return (deriv_f.subs(x, tabular_point(f_eq, problem_point))) * (problem_point - tabular_point(f_eq, problem_point)) + f_eq.subs(x, tabular_point(f_eq, problem_point))


def original_graph_plotter(function_equation, problem_point, option_point=1):
    variables_x = []
    variables_y = []

    if option_point == 1:
        for i in range(0, problem_point + 1):
            function_result = function_equation.subs(x, i)
            la_function_result = linear_value_approximator(i)

            variables_x.append(i)
            variables_y.append([function_result, la_function_result])
    elif option_point == 2:
        for i in range(0, problem_point + 1):
            function_result = function_equation.subs(x, i)
            ta_function_result = taylor_polynomial_function(i, option_point)


            variables_x.append(i)
            variables_y.append([function_result, ta_function_result])

    plt.title("Graph of the original function and the approximated function")
    plt.xlabel("x-variables")
    plt.ylabel("y-variables")
    plt.plot(variables_x, variables_y)
    plt.savefig("Gradient_graph.jpg")