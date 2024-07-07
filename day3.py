# python dictionery
'''
students = {   
"11":["suren","surendra"],
"12":["suren"]
    
}

print(students["1"][:1])

'''

# list of birds and animals
'''
jungle = {
"animal" : ['tiger','lion'],
"birds"  : ['pigeon','parrot'],
"insects" :[ {
    'name':'cockroach',
    'scientific name':'blattodea',
    'life spam':'3 years'
},{
    "name": "ant",
    "scientific name":"formicidae",
    "life spam":"1 years"
}]
}

jungle.update({
    "new": "don"
    
})
print(jungle)
    
print(jungle['insects'])
'''
# asking the roll no and name from user and give me result as {1:"ram", 2: "hari"}
'''
input1_name = input("enter your name:")
input1_rollno= input("enter roll no:")

input2_name = input("enter your name:")
input2_rollno= input("enter roll no:")

students = {}
students.update({
    input1_name: input1_rollno,
    input2_name: input2_rollno,
})
students.update({
    "students":[input1_name,input2_name],
    "rollno":[input1_rollno,input2_rollno],

})
print (students)
'''
