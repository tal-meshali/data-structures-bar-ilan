import re
import pandas as pd
import numpy as np


def build_function():
    x = input()
    lst = re.findall(r"([\+\*-]?)(\d*)\*?([xyzw]\d?)*", x)
    result = dict()
    for sign, scal, var in lst:
        val = 0
        if sign == '-':
            val = -1
        else:
            val = 1
        if scal != '':
            val *= int(scal)
        if var != '':
            result[var] = [val]
    return result


def build_constraints():
    constraints = []
    i = 0
    x = input()
    while x != 'X':
        constraints.append(dict())
        lst = re.findall(r"([\+\*-]|<=|>=)?(-?\d*)\*?([xyzw]\d?)*", x)
        for sign, scal, var in lst:
            if sign == '-':
                val = -1
            else:
                val = 1
            if scal != '':
                val *= int(scal)
            if var != '':
                constraints[i][var] = val
            else:
                if scal != '':
                    constraints[i][sign] = scal
        i += 1
        x = input()
    return constraints


def build_matrix_dictionary(result, constraints):
    for i in range(1, len(constraints) + 1):
        result["w" + str(i)] = [0]
    result["final"] = [0]
    for i in range(len(constraints)):
        for key in result.keys():
            if re.match(r"w\d", key):
                if int(re.findall(r"w(\d)", key)[0]) == i + 1:
                    result[key] += [1]
                else:
                    result[key] += [0]
            elif key == "final":
                if ">=" in constraints[i].keys():
                    result[key] += [(int(constraints[i][">="]), ">=")]
                else:
                    result[key] += [(int(constraints[i]["<="]), "<=")]
            elif key in constraints[i].keys():
                result[key] += [constraints[i][key]]
            else:
                result[key] += [0]
    return result


def main():
    print("Hello there, please enter the amount of variables the problem consists of:")
    n_var = int(input())
    print("Now enter the maximization problem, in the form of x1+3*x2+...")
    result = build_function()
    print("Now enter your constraints in the form of x1+3*x2+...<=b, to stop type X:")
    constraints = build_constraints()
    print(get_solution(make_matrix(n_var, build_matrix_dictionary(result, constraints))))


def make_matrix(num, d):
    matrix = pd.DataFrame.from_dict(d)
    for i, row in matrix.iterrows():
        if i > 0:
            if row["final"][1] == ">=":
                matrix.at[i, "final"] = row["final"][0]
                matrix.loc[i] = row * (-1)
            else:
                matrix.at[i, "final"] = row["final"][0]

    while max(matrix.loc[0][0:num]) > 0:
        print(matrix)
        # Dual case
        if np.min(matrix["final"][1:]) <= 0:
            max_b = np.argmin(matrix["final"][1:]) + 1
            current_row = matrix.loc[max_b]
            row_lst = [0 if current_row[i] >= 0 else -1 / current_row[i] for i in range(len(current_row) - 1)]
            max_row = np.max(row_lst)
            if max_row > 0:
                max_a = np.argmin([max_row + 1 if x == 0 else x for x in row_lst])
                matrix.loc[max_b] /= matrix.loc[max_b][max_a]
                for i, row in matrix.iterrows():
                    if i != max_b and row[max_a] != 0:
                        matrix.loc[i] = row / row[max_a] - matrix.loc[max_b]
            else:
                return False
        # Regular case
        else:
            current_row = matrix.loc[0][0:num]
            max_c = np.argmax(current_row)
            if current_row[max_c] <= 0:
                return matrix, num
            current_column = matrix.iloc[:, max_c].tolist()
            row_lst = [0 if matrix.iloc[:, max_c][x] == 0 else matrix.loc[x]["final"] / matrix.iloc[:, max_c][x] for x
                       in range(len(current_column))]
            max_row = np.max(row_lst)
            if max_row > 0:
                min_element = np.argmin([max(row_lst) + 1 if x <= 0 else x for x in row_lst])
                matrix.loc[min_element] /= matrix.iloc[:, max_c][min_element]
                for i, row in matrix.iterrows():
                    if i != min_element and row[max_c] != 0:
                        matrix.loc[i] = row / row[max_c] - matrix.loc[min_element]
            elif check_finished_column(max_c, matrix) >= 0:
                return matrix, num
            else:
                return False
    return matrix, num


def check_finished_column(i, matrix):
    true_var = -1
    for j in range(matrix.shape[0]):
        if matrix.loc[j][i] == 1 and true_var == -1:
            true_var = j
        elif matrix.loc[j][i] != 0.0 or matrix.loc[j][i] != -0.0:
            true_var = -1
            break
    return true_var


def get_solution(sol):
    if not sol:
        return "There is no solution."
    matrix, num = sol
    result = []
    for i in range(num):
        true_var = check_finished_column(i, matrix)
        if true_var >= 0:
            result.append((matrix.columns[i], matrix.loc[true_var]["final"]))
    return result


main()
