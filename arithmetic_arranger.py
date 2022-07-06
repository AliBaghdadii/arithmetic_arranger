def arithmetic_arranger(list_of_the_problems, giving_answer = False):
    #  we can not use 5 problems or more
    if len(list_of_the_problems) > 5:
        return "Error: Too many problems."

    # only we can use this operators
    operators = ("+", "-")

    # we create a list for each line in our output
    first_line, second_line, third_line, fourth_line = [], [], [], []

    for problem in list_of_the_problems:
        operation = problem.split(" ")

        # maybe the given operator is not in the tuple we created in line 7
        if operation[1] not in operators:
            return "Error: Operator must be '+' or '-'."

        # create values for doing our operates
        first_number = operation[0]
        second_number = operation[2]

        # we must use integers as our numbers
        if first_number.isdigit() == False or second_number.isdigit() == False :
            return "Error: Numbers must only contain digits."

        # we can not use any number and the len of our number must be less than 5
        if len(first_number) > 4 or len(second_number) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Max spaces to fill in the final print. We find the longest number and we add the operator's space and the space btw the operator and the second element
        max_spaces_to_fill = max(len(i) for i in operation)
        dash = "-"
        space = " "

        # first number and we add 4 spaces between each operation
        first_line.append(first_number.rjust(max_spaces_to_fill+2)+ space*4)
        # operator, space and second number
        second_line.append(operation[1] + space + second_number.rjust(max_spaces_to_fill)+space*4)
        # dash line
        third_line.append(dash * (max_spaces_to_fill+2)+space*4)
        # the result if giving_answer is True
        result = (str(eval(problem)))
        fourth_line.append(result.rjust(max_spaces_to_fill+2)+space*4)

    # Transform each list in string
    first_line = ''.join(map(str, first_line))
    second_line = ''.join(map(str, second_line))
    third_line = ''.join(map(str, third_line))
    fourth_line = ''.join(map(str, fourth_line))
    # we will print answer
    if giving_answer == True:
        arranged_problems = first_line + "\n" + second_line + "\n"+ third_line + "\n"+ fourth_line
    # we only print the operation
    if giving_answer == False:
        arranged_problems = first_line + "\n" + second_line + "\n"+ third_line
    print(arranged_problems)
    return arranged_problems
