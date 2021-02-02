from workplace import waterRefill # <- - - - - - - Workplace Function
import sys

# dont touch this stuff 

taskNum = 9 # <- - - - - Task Number
numtasks = 4 # <- - - - - Number of tasks, also edit files
variables = {}
perfect = True

for i in range(1, numtasks+1):
  # Argument formatting
  testCase = open(("TestCases/testCase" + str(i) + ".py"), "r").readlines()

  size = float(testCase[0])
  filled = float(testCase[1])

  print("---------- test" + str(i) + " ----------")
  variables["t{0}t".format(i)] = open(("TaskResults/task" + str(i) + "Test.py"), "r").read()

  # Workplace Function Name - - -> arg - -> 
  variables["t{0}a".format(i)] = waterRefill(size, filled)

  if variables["t{0}t".format(i)] == variables["t{0}a".format(i)]:
    print("|         Success         |")
  else:
    print("|       You failed.       |")
    perfect = False

print("---------------------------")

if perfect == True:
  print("\nCongratulations! You successfully completed PPSC_task_" + str(taskNum))
