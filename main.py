def arithmetic_arranger(problems, show_answers=False):
    arithmetic = {"num1":[], "symb":[], "num2":[]}
    for i in problems:
        problem = i.split()
        arithmetic["num1"].append(problem[0])
        arithmetic["symb"].append(problem[1])
        arithmetic["num2"].append(problem[2])
    #Перевірка проблем
    if len(problems) > 5:
        return 'Error: Too many problems.'
    if not len(arithmetic["symb"]) == arithmetic["symb"].count("+") + arithmetic["symb"].count("-"):
        return "Error: Operator must be '+' or '-'." 
    for i in range(len(arithmetic['num1'])):
        if not arithmetic["num1"][i].isdigit() or not arithmetic["num2"][i].isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(arithmetic["num1"][i]) > 4 or len(arithmetic["num2"][i]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
    return arithmetic

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')