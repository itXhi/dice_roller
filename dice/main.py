import random

def roll():
      dice = random.randint(1,6)
      if dice == 1 :
       print("---------")
       print("|       |")
       print("|   *   |")
       print("|       |")
       print("---------")
      elif dice == 2:
        print("---------")
        print("| *     |")
        print("|       |")
        print("|     * |")
        print("---------")
      elif dice == 3 :
        print("---------")
        print("| *     |")
        print("|   *   |")
        print("|     * |")
        print("---------")
      elif dice == 4:
        print("---------")
        print("| *   * |")
        print("|       |")
        print("| *   * |")
        print("---------")
      elif dice == 5  :
        print("---------")
        print("| *   * |")
        print("|   *   |")
        print("| *   * |")
        print("---------")
      elif dice == 6:
        print("---------")
        print("| *   * |")
        print("| *   * |")
        print("| *   * |")
        print("---------")
   
def main():
  choice = input("DO you want to roll a dice(Y/N) : ").lower()
  if choice == "y":
    try:
      num = int(input("How many number of rolls : "))
      for i in range(num):
        roll()
      
    except:
      print("Please enter vaild number")
  else:
    print("Thanks for visiting!")    

if __name__ == "__main__":
  main()

while True:
  main()
  again = input("Do you want to roll again(Y/N)").lower
  if again != "y":
    break
  