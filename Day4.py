# conditional statement
my_dict = {
    '1':'ram',
    '2':'shyam'
}

my_keys = my_dict.keys()# ["1","2"]
my_values=my_dict.values()#["ram","shyam"]

roll_no = input("enter roll no:")

if roll_no in my_keys : # true
        print("key already exists")
        print("ok executed")
else:
    name = input("enter name:")
    
    if name in my_values:
        print("name already exicts")
    else :
        print('nope')
my_dict.update({
                roll_no:name
            })
    
print("my students",my_dict)

   
 
    
    
    