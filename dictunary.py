file = {
    "name" : "noor",
    "age" : 89,
    "uni" : "peshawar",
    "marks" : [89,98,100,76,34]
}


# nested dictionay 
Student = {
    "name" : "abdullah",
    "Subject" : {
        "English" : 90,
        "architechture" : 89,
        "calculus" : 77
    }
}
print(file.keys())
print(list(file.keys()))
print("total keys are: " ,len(list(file.keys())))

print(Student.keys())
print(list(Student.keys()))
print("Total keys in Student are : ", len(list(Student.keys())))




