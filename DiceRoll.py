#DiceRoll.py
#Name: Miguel Alvarado
#Date: 2/26/2026
#Assignment: Lab 6
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  trails = 10000
  #Create two dice values ranging from 1 - 6 each
  for r in range(trails):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
  #find the sum total of the two dice
    total = dice1 + dice2
    rolls[total - 2] = rolls[total - 2] + 1
  #print statictics for dice rolls
  for total in range (2,13):
     count = rolls[total - 2]
     percentage = (count / trails)*100
     print(total, ":", count, ":", round(percentage,2),"%")

if __name__ == '__main__':
  main()
