import string

def eat_pizza(eat, pizza):
  while eat.lower() == "yes":
    if pizza != 0:
      pizza = pizza - 1
      print(str(pizza) + " slices left")
      eat = input("Do you want to eat another slice?")
    else:
      print("Sorry, No more pizza left!")
      break

pizza = 8
eat = input("The pizza's delivered! Do you want to eat a slice of pizza?")
eat_pizza(eat, pizza)