name = input("Name : ")
gender = input(("male-1/Female -2"))
email = input("Email : ")


print("[user_information]")
print(f"name: {name}")
print(f"gender: {"male" if gender =="1" else "female"}")
print(f"email: {email}")
