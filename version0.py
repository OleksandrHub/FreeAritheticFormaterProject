def arithmetic_arranger(problems, show_answers=False):
    arithmetic = {"num1":[], "symb":[], "num2":[], "len-line":[], "result":[]}
    for i in problems:
        problem = i.split()
        arithmetic["num1"].append(problem[0])
        arithmetic["symb"].append(problem[1])
        arithmetic["num2"].append(problem[2])
        arithmetic["result"].append(str(eval(i)))

    length = len(problems)
    del problems
    #Перевірка помилок та Знаходження максимальної довжини лінії
    if length > 5:
        return 'Error: Too many problems.'
    if not len(arithmetic["symb"]) == arithmetic["symb"].count("+") + arithmetic["symb"].count("-"):
        return "Error: Operator must be '+' or '-'." 
    for i in range(length):
        len_number_1 = len(arithmetic["num1"][i])
        len_number_2 = len(arithmetic["num2"][i])
        if not arithmetic["num1"][i].isdigit() or not arithmetic["num2"][i].isdigit():
            return 'Error: Numbers must only contain digits.'
        if len_number_1 > 4 or len_number_2 > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if len_number_1 > len_number_2:
            arithmetic["len-line"].append(len_number_1 + 2)
        else:
            arithmetic["len-line"].append(len_number_2 + 2)

    #Виведення результату
    result = ''
    for i in range(length):
        result += " "*(arithmetic["len-line"][i]-len(arithmetic["num1"][i]))+arithmetic['num1'][i]+"\t"
    result += '\n'
    for i in range(length):
        result += arithmetic["symb"][i]+" "*(arithmetic["len-line"][i]-len(arithmetic["num2"][i])-1)+arithmetic['num2'][i]+"\t"
    result += '\n'
    for i in range(length):
        result += "-"*arithmetic["len-line"][i] + '\t'
    if show_answers:
        result += '\n'
        for i in range(length):
            result +=" "*(arithmetic["len-line"][i]-len(arithmetic["result"][i]))+arithmetic['result'][i]+"\t"
    return result

print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"],False)}')