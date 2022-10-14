
def isValid(num):
  numString = input("type a number: ")
  numString = str(num)
  validNum = ["1", "6", "9", "8"]
  rotation = {
    "1" : "1",
    "6" : "9",
    "9" : "6",
    "8" : "8"
    }

  for i in range(len(numString)//2+1):
    currentValue = numString[i]
    other = numString[len(numString)-(i+1)]
    if currentValue in validNum:
      if rotation[currentValue] != other:
        return False
      else:
        return False

  return True
isValid()

