def Score(word: str) -> int:
  
  scoreGuide = {
    "aeioulnstrавеинорст": 1,
    "dgдклмпу": 2,
    "bcmpбгёья": 3,
    "fhvwyйы": 4,
    "kжзхцч": 5,
    "jxшэю": 8,
    "qzфщъ": 10
  }
  
  totalScore = 0
  
  for letter in word:
    for key in scoreGuide:
      
      if letter in key:
        totalScore += scoreGuide[key]
  
  return totalScore

while True:
  try:
    userWord = str(input('enter your word: ').lower())
    userScore = Score(userWord)
    print(f'your score -> {userScore}')
    break
  except:
    print('Oops! Invalid input. Try again..')