def formation_of_results(data, line, result, symb=[" "]*5):
    for i in range(len(data)):
        data[i] = symb[i] + " " * (len(line[i])-len(data[i])-1)+data[i]
    result += "    ".join(data)+"\n"
    return result

def add_to_data(data,keys,values):
    for i in range(len(keys)):
        data[keys[i]].append(values[i])
    return data

def arithmetic_arranger(problems, show_answers=False):
    length = len(problems)
    #Помилка довжина масиву
    if length > 5:
        return 'Error: Too many problems.'
    #Встановлення даних
    data = {"num1":[], "symb":[], "num2":[], "line":[], "result":[]}
    for i in problems:
        result = i.split()
        len_number_1, len_number_2 = len(result[0]),len(result[2])
        #Перевірка помилок 
        if len_number_1 > 4 or len_number_2 > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not result[0].isdigit() or not result[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if not(result[1] == "+" or result[1] == "-"):
            return "Error: Operator must be '+' or '-'." 
        #Додавання даних
        result.append(str(eval(i)))
        data = add_to_data(data, ["num1","symb","num2","result"],result)
        if len_number_1 > len_number_2:
            data = add_to_data(data, ['line'], ["-"*(len_number_1 + 2)])
        else:
            data = add_to_data(data, ['line'], ["-"*(len_number_2 + 2)])
    del result, len_number_1, len_number_2
    
    result = ''
    result = formation_of_results(data["num1"], data['line'], result)
    result = formation_of_results(data["num2"], data['line'], result, data['symb'])
    result += "    ".join(data["line"])

    if show_answers:
        result += "\n"
        result = formation_of_results(data["result"], data['line'], result)
        result = result[:-1]
    return result

print(f'{arithmetic_arranger(["3801 - 2", "123 + 49" ],True)}')