import time

#-----------

def Introduction():
  print("Welcome to Percentage Calculator. You will be able to convert two numbers into a percentage.\nFor example, the program will return 50% if your inputs are 1 and 2, or 5 and 10, or more. Decimal numbers are rounded to the first digit.")

def Calculate(value1, value2):
  return (value1/value2)*100
  
#-----------

Introduction()
time.sleep(1)
while True:
  _value1 = input("\n--------------------------\nEnter your first value below. For example, it represents the 50 in \"50 out of 100\" for 50%.\n>>>\t")
  _value2 = input("\nEnter your second value below. For example, it represents the 100 in \"50 out of 100\" for 50%.\n>>>\t")
  try:
    _value1 = round(float(_value1),1)
    _value2 = round(float(_value2),1)
  except ValueError:
    print("Error using your inputs. Have you entered valid numbers ? (Examples : 33.6 / 90 / 10000)")
  _valuex = round(Calculate(_value1, _value2),1)
  if _value1.is_integer() == True:
    _value1 = int(_value1)
  if _value2.is_integer() == True:
    _value2 = int(_value2)
  if _valuex.is_integer() == True:
    _valuex = int(_valuex)
  print("\n* " + str(_value1) + " out of " + str(_value2) + " represents " + str(_valuex) + "%.")
  time.sleep(2)