students = ["John",23,"24 Somewhere Lane UK","Cardiff","+44 0123456789"]
student_details = {
    "name":"John",
    "age":23,
    "address":"24 Somewhere Lane UK",
    "city":"Cardiff",
    "phone_number":"+44 0123456789"
}
print(student_details)
print(student_details["name"])
print(student_details.keys())
print(student_details.values())
for key in student_details.keys():
    print(key,"|",student_details[key])
if "city" in student_details:
    print(student_details["city"])
else:
    print("City not found.")
student_details["height"] = 158
print(student_details)
del student_details["city"]
print(student_details)
student_details["marks"] = [80,90,93,59,70]
print(student_details)
print(student_details["marks"][1])
classroom = {
    "John":{
    "age":23,
    "address":"24 Somewhere Lane UK",
    "city":"Cardiff",
    "phone_number":"+44 0123456789"    
},
    "Shaun":{
    "age":22,
    "address":"23 Somewhere Lane UK",
    "city":"Swansea",
    "phone_number":"+44 9876543210"
},
    "Shaun":{
    "age":21,
    "address":"22 Somewhere Lane UK",
    "city":"Leicester",
    "phone_number":"+44 1357986420"
}
}




