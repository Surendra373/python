num1 = 20
num2 = 30
num3 = 10
def menu():
    print ("press \n a = add \n s = subtract \n  m = multiply \n d = divide \n e = exit ")
  
def ask_user_input():
    user_input = input ("select a opinion from above:")
    return user_input

def add():
    return num1 + num2 + num3
  
def sub():
    return num1 - num2 - num3
  
def mul():
    return num1 * num2 * num3
  
def div():
    return num1/num2

if __name__ == "__main__":
    menu()
    user_input = ask_user_input()
    add_output = sub_output = mul_output = div_output = 0
    while user_input in ('a','s','m','d'):
        if user_input == 'a':
            add_output = add()
        elif user_input == 's':
            sub_output = sub()
        elif user_input == 'm':
            mul_output = mul()
        elif user_input == 'd':
            div_output = div()
            
        else:
            break
        menu ()
        user_input = input ("do you want to continue:")
        print (f"result: \n addition : {add_output} \n subtraction:{sub_output} \n multiplication : {mul_output} \n division : {div_output} ")
            
  
    