from graph_executor import f_eq, x, tabular_point, linear_value_approximator, taylor_polynomial_function, original_graph_plotter
import sys
decimal_num = 0

if __name__ == "__main__":
    option_num = int(sys.argv[1])

    try:
        if option_num == 1:
            # Please enter your problem point
            prob_point = int(sys.argv[2])

            print(
                f"Tabular point: {tabular_point(f_eq, prob_point)} \nActual value: {f_eq.subs(x, prob_point)} \nApproximate value: {linear_value_approximator(prob_point)}")

            if f_eq.subs(x, prob_point) == linear_value_approximator(prob_point):
                print("The program is correct nth decimal places.")
            else:
                while round(f_eq.subs(x, prob_point), decimal_num) - round(linear_value_approximator(prob_point),
                                                                           decimal_num) == 0:
                    decimal_num += 1

                if decimal_num == 0:
                    if (f_eq.subs(x, prob_point) > linear_value_approximator(prob_point)) or (f_eq.subs(x, prob_point) < linear_value_approximator(prob_point)):
                        print("Points are far apart from one another.")
                else:
                    print(f"The program is correct to {decimal_num} decimal places.")
        elif option_num == 2:
            prob_point = int(sys.argv[2])

            # To which polynomial order would you like your function to approximate values to
            polynomial_order = int(sys.argv[3])

            print(
                f"Tabular point: {tabular_point(f_eq, prob_point)} \nActual value: {f_eq.subs(x, prob_point)} \nApproximate value: {taylor_polynomial_function(prob_point, polynomial_order)}")

            if f_eq.subs(x, prob_point) == taylor_polynomial_function(prob_point, polynomial_order):
                print("The program is correct nth decimal places.")
            else:
                while round(f_eq.subs(x, prob_point), decimal_num) - round(taylor_polynomial_function(prob_point, polynomial_order), decimal_num) == 0:
                    decimal_num += 1
                
                if decimal_num == 0:
                    if (f_eq.subs(x, prob_point) > taylor_polynomial_function(prob_point, polynomial_order)) or (f_eq.subs(x, prob_point) < taylor_polynomial_function(prob_point, polynomial_order)):
                        print("Points are far apart from one another.")
                else:
                    print(f"The program is correct to {decimal_num} decimal places.")
        else:
            print("Please choose one of the option available (1 or 2).")

        original_graph_plotter(f_eq, prob_point, option_num)
    except (ValueError, TypeError):
        print("Please enter the correct data type: int (numbers).")
    except IndexError:
        print("It seems like you have chosen the Taylor Approximation method, this methods excpects three arguments (problem point problem point polynomial_order). Please enter all the required arguments.")