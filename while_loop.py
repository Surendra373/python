# while loop

appended_number = []
user_input = input("enter your name:")

while user_input.isdigit():
    user_input= input("enter number:")
    appended_number.append(user_input)
    
    print(appended_number)
    
    