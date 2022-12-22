import random
def RandomList(size: int):
  
  resultList = []
  for _ in range(size):
    rndNum = random.randint(1, 9)
    resultList.append(rndNum)
  return resultList

def NearestNum(num: int, array: list):
  result = min(array, key = lambda arrayI: [abs(arrayI - num), arrayI])
  return result

while True:
  try:
    digitsNum = int(input('enter the number of digits: '))
    taskList = RandomList(digitsNum)
    print(f'generated sequence: {taskList}')
    
    requiredNum = int(input('enter a number to search nearest occurrence: '))
    result = NearestNum(requiredNum, taskList)
    print(f'nearest occurrence: {result}')
    break

  except:
    print('Oops! Incorrect input. Try again..')