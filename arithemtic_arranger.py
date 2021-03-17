def arithmetic_arranger(problems, answer = None):
    import re

    first_line = ""
    second_line = ""
    separator_line = ""
    answers_line = ""
    problems_count = 0

    for problem in problems:

        problems_count += 1

        if problems_count > 5:
            return "Error: Too many problems."

        item = re.findall('\S+', problem)

        #outputs for printing cols--these are strings!
        str_num1 = item[0]
        str_op = item[1]
        str_num2 = item[2]

        if str_op != "+" and str_op != "-":
            return "Error: Operator must be '+' or '-'."
            

        if len(str_num1) > 4 or len(str_num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        #outputs for calculation--these are integers
        try:
            int_num1 = int(item[0])
            int_num2 = int(item[2])
        except:
            return "Error: Numbers must only contain digits."

        #lookup table for converting +/- strings to operators
            #use example: print(ops["+"], (int_num1, int_num2)
        ops = {"+": lambda x, y: x + y,
               "-": lambda x, y: x - y}

        #get the column width based on the longest of two numbers
        col_width = max(len(str_num1), len(str_num2))

        #output for printing of column operation
        first_line += str_num1.rjust(col_width + 2)
        first_line += "    "
        second_line += str_op.ljust(1)
        second_line += str_num2.rjust(col_width + 1)
        second_line += "    "
        separator_line += ("-" * (col_width + 2))
        separator_line += "    "

        #answer calculation
        ans = ""
        if str_op == "+":
                ans = ops['+'](int_num1, int_num2)

        else:
                ans = ops['-'](int_num1, int_num2)
        
        answers_line += (str(ans).rjust(col_width + 2))
        answers_line += "    "
        
    first_line = first_line.rstrip()
    second_line = second_line.rstrip()
    separator_line = separator_line.rstrip()
    answers_line = answers_line.rstrip()
    

    arranged_problems = first_line + "\n" + second_line + "\n" + separator_line

    if answer == True:
      arranged_problems += "\n" + answers_line

    return arranged_problems
