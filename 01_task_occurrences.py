import random


def RandomList(num: int):
  resultList = []
  for _ in range(num):
    rndNum = random.randint(0, 5)
    resultList.append(rndNum)
    
  return resultList

def Occurrences(num: int, array: list):
  count = 0
  for number in array:
    if number == num:
      count +=1
  return count

while True:
  try:
    
    digitsNum = int(input('enter the number of digits: '))
    taskList = RandomList(digitsNum)
    print(taskList)
    
    requiredNum = int(input('enter a number to search for: '))
    numOccurrence = Occurrences(requiredNum, taskList)
    
    print(f'the number of occurrences of a number in the generated list -> {numOccurrence}')
    break
  except:
    print('Oops! Incorrect input. Try again..')