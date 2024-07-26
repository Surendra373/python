# file
# for i in range(1,10):
    
#     f=open("student_name","w")
#     f.write(" name:surendra \t rollno: 11 \n")
#     f.close()

# # with statement
# with open ("student_rollno","a") as f:
#     f.write("name:surendra\n rollno:11\t ")
    
    
with open ("student_rollno","r") as f:
    print(f.read())