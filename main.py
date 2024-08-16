import time

def print_pause(text):
    print(text)
    time.sleep(3)                                                                                                                                                                                
def get_numeric_input(prompt):
      while True:
        user_input = input(prompt)
        if user_input.isdigit():
          return float(user_input)
        else:
          print("Invalid input. Please enter a number.")

def main():
    userName = input("Enter your name: \n ")
    while userName.isalpha() == False:
        print_pause("invalid input. Please enter a valid name")
        userName = input("Enter your name: \n ")
    print_pause("Welcome " + userName)
    get_bmi()

def get_bmi():
    height = get_numeric_input("Enter your height in cm: ")
    while height < 60 or height > 210:
        print("Invalid input entered")
        height = get_numeric_input("Enter your height in cm: ")
    weight = get_numeric_input("Enter your weight in kilograms: ")
    while weight < 20 or  weight > 250:
        print("Invalid input entered")
        weight = get_numeric_input("Enter your weight in kilograms: ")
    height2 = height/100
    height2 = height2 * height2
    BMI = weight / height2
    print_pause("Your BMI is " + str(BMI))
    if BMI < 18.5:
        print_pause("You may be underweight")
        print_pause("Try excercising more often, eating healthy food like vegetables and fruits and consuming between 4000-5000 calories per day.\n")
        print_pause("Our professional team recommends visiting our website Be Healthy for more tips!!")
    elif BMI >= 18.5 and BMI < 25:
        print_pause("You are fit !")
        print_pause("Try excercising more often to keep fit, eating healthy food like vegetables and fruits and consuming between 2000-3000 calories per day.\n")
        print_pause("Our professional team recommends visiting our website Be Healthy for more tips!!")

    elif BMI >= 25 and BMI < 45:
        print_pause("You may be overweight.\n")
        print_pause("Try excercising more often, eating healthy food like vegetables and fruits and consuming between 2000-3000 calories per day.\n")
        print_pause("Our professional team recommends visiting our website Be Healthy for more tips!!")
    elif BMI >= 45:
        print_pause("You may be obese.\n")
        print_pause("Try excercising more often, eating healthy food like vegetables and fruits and consuming between 2000-3000 calories per day.\n")
        print_pause("Our professional team recommends visiting our website Be Healthy for more tips!!")
    healthy_recipes()

def healthy_recipes():
    userInput = input("Would you like us to recommend some healthy recipes for you to try?(y/n)\n").lower()
    while userInput not in ["y","n"]:
        print_pause("Invalid input. Please enter y or n.")
        userInput = input("Would you like us to recommend some healthy recipes for you to try?(y/n)\n").lower()
    
    if userInput == "y":
         print_pause("Okay, let's recommend some healthy recipes!\n")
         print_pause("For  breakfast, You can have Healthy pancakes along side a fruit of your choice.")
         print_pause("For lunch, you can have protein of your choice with rice and salad.")
         print_pause("For a quick snack, you can make a healthy smoothie made with diffrent kinds of fruits.")
         print_pause("For dinner, you can have greek yogurt rich in high protein.")
         print_pause("Hope you try these delicious recipes!")
         play_again()
    elif userInput == "n":
        print_pause("Alright")
        play_again()

def play_again():
    userInput = input("Would you like to play again?(y/n)\n").lower()
    while userInput not in ["y","n"]:
        print_pause("Invalid input. Please enter y or n.")
        userInput = input("Would you like to play again?(y/n)\n").lower()
    if userInput == "y":
        print_pause("Okay!")
        main()
    elif userInput == "n":
        print_pause("Okay then, thank you for using our service!")

main()