#Functions
def addition(num1,num2):
   answer = num1 + num2
   print("The sum of the two numbers is" , answer)

def subtraction(num1,num2):
  answer = num1 - num2
  print("The sum of the two numbers is" , answer)

def multiplication(num1,num2):
  answer = num1 * num2
  print("The sum of the two numbers is" , answer)

def division(num1,num2):
  if num1 == 0:
    print("Math error")
  else:
      answer = num1 / num2
      print("The sum of the two numbers is" , answer)

#CALCULATOR MENU
while True:
  print("CALCULATOR MENU : Please select a Mathematical Operation ")
  print("1. ADDITION")
  print("2. SUBTRACTION")
  print("3. MULTIPLICATION")
  print("4. DIVISION")


  #A user selecting their desirable operation type
  operation_type = int(input("Enter the corresponding number of the operation type :"))

  #Invalid Choice
  num1 = float(input("First Number"))
  num2 = float(input("Second number :"))

  #Addition
  if operation_type == 1:
      addition(num1,num2)

  #Subtraction
  elif operation_type == 2:
      subtraction(num1,num2)

  #Multiplication
  elif operation_type == 3:
      multiplication(num1,num2)

  #Division
  elif operation_type == 4:
      division(num1,num2)

  else: 
      print("Your selection is not valid")
