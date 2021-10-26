import random

def PopulateLogFile(totalLines = 10000):
  countries = ["52", "55", "56"]
  allStatus = ["cancelado", "assinado"]

  file = open('log.txt', 'w')


  for _ in range (totalLines):
    country = countries[random.randint(0,2)]
    code = str(random.randint(100000000000,999999999999))
    status = allStatus[random.randint(0,1)]
    file.write(country+code + " " + status + "\n")

  file.close()

PopulateLogFile()