def arithmetic_arranger(problems, show_results=False):
  # Checking the number of problems and raising an Error if more than 5
  if len(problems) > 5:
    #raise Exception("Error: Too many problems.")
    return "Error: Too many problems."

  # Analysing the operations and raising erros
  operations = list()
  i = 0
  for problem in problems:
    operations.append(problem.split())
    #evaluating the operations signs
    if operations[i][1] not in ("+", "-"):
      #raise Exception("Error: Operator must be '+' or '-'.")
      return "Error: Operator must be '+' or '-'."

    #raising the error for incorrect integers
    if not operations[i][0].isdigit() or not operations[i][2].isdigit():
      #raise Exception("Error: Numbers must only contain digits.")
      return "Error: Numbers must only contain digits."

    #raising the error for incorrect length of integers
    if len(operations[i][0]) > 4 or len(operations[i][2]) > 4:
      #raise Exception("Error: Numbers cannot be more than four digits.")
      return "Error: Numbers cannot be more than four digits."

    i += 1

  # Getting the operations' maximum lenght
  ops_lenght = list()
  i = 0
  for operation in operations:
    #converting the strings to integers
    operations[i][0] = int(operations[i][0])
    operations[i][2] = int(operations[i][2])

    #moving the operation sign to the end
    operation.append(operation.pop(1))

    #getting the lenght of the highest number for each operation
    ops_lenght.append(len(str(max(operation[0:2]))))

    i += 1

  # Calculating the right alignment for each operation
  right_just = list()
  for op_len in ops_lenght:
    right_just.append(op_len + 2)

  # Setting the dashed line for each operation
  dash_lines = list()
  i = 0
  for op in ops_lenght:
    dash_line = str((op * "-") + 2 * "-").rjust(right_just[i])
    dash_lines.append(dash_line)
    i += 1

  # Calculating the operations results and setting them to be printed
  results = list()
  i = 0
  for operation in operations:
    if operation[2] == "+":
      result = operation[0] + operation[1]
    elif operation[2] == "-":
      result = operation[0] - operation[1]
    result = str(result).rjust(right_just[i])
    results.append(result)
    i += 1

  # Setting up the printing of the arithmetic problems
  #seting the first line
  line_1 = list()
  i = 0
  for operation in operations:
    line_1.append(f"{str(operation[0]).rjust(right_just[i])}")
    i += 1

  #setting the second line
  line_2 = list()
  i = 0
  for operation in operations:
    spaces = ops_lenght[i] + 1 - len(str(operation[1]))
    string = str(operation[2]) + spaces * " " + str(operation[1])
    line_2.append(string)
    i += 1

  #setting the possible arrangements
  #for show_results = False
  arrang_f = ("    ".join(map(str, line_1)) + "\n" + "    ".join(line_2) +
              "\n" + "    ".join(dash_lines))

  #for show_results = True
  arrang_t = ("    ".join(map(str, line_1)) + "\n" + "    ".join(line_2) +
              "\n" + "    ".join(dash_lines) + "\n" +
              "    ".join(map(str, results)))

  if show_results == False:
    arranged_problems = arrang_f
  elif show_results == True:
    arranged_problems = arrang_t

  return arranged_problems
