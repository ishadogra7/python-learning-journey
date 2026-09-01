# dictionary ==> contins a key : value which help in accessing 


 # basic create and access
student = {
    "name" : "isha" ,
    "age" : 29  ,
    "course" : "btech" ,
    "branch" : "CSE" ,
    "location" : "dehradun"
      }
    
print(student["name"])
print(student.get("age"))
print(student.get("name"))
print(student.get("city" ,"NOT FOUND"))
print(student.get("city","Unknown"))

# add new value
student["phone"] = "11111-111111"
print(student.get("phone","unknown"))

# it update the value by remmving the place value
student["name"] = "dogra"
print(student["name"])
print(student)

       # for multiple update value
student.update({"age" : 40 , "phone" : 5565656})
print(student)


#  delte the age
del student["age"]
print(student)

# keys & values
print(student.keys())
print(student.values())

# items used for the pairung keys annd values
print(student.items())

# looping
for keys, values in student.items():
    print(keys , "->" ,values)


# Nested looping
student = {
    "student1" : {"name" : "amit" ,"age":56}  ,
    "student2" : {"name" : "radhe" , "age" :45}
}

print(student["student2"]["age"])
print(student["student1"]["name"])
# looping throgh  nested dictonary

for student_id , details in student.items():
    print(student_id)
    print("Name-->", details["name"] )
    print("Age -->" , details["age"])