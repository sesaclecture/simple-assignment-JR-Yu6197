import json

name = input("Enter your name: ")
gender = input("Enter your gender? \nex) Male - M,Female - F ")
email = input("Enter your email: ")
contact = input("Enter your contact: ")
address = input("Enter your address: ")
subject = input("Enter your subject: ")



b_6digit = int(input("Enter your birth 6 digit(ex. 990101): "))


age = 2025 - (b_6digit // 10000 + 1900) + 1



project_a = {
    "name" : "Project A",
    "subject" : "Language",
    "skill" : "Python",
    "duration" : "21 days",
    "detail" : "This is a project to learn Python programming."
}

project_b = {
    "name" : "Project B",
    "subject" : "Data Analysis",
    "skill" : "Pandas",
    "duration" : "30 days",
    "detail" : "This is a project to learn Data Analysis using Pandas."
}

skills = ["Python", "Java", "C++"]
interests = ["music", "movie", "reading"]


user_info_1 = {
    "name": name,
    "gender": gender
    ,"email": email
    ,"contact": contact
    ,"address": address
    ,"subject": subject
    ,"age": age
    ,"birth_6digit": b_6digit
    ,"interests" :  interests
    ,"skills" : skills 
    ,"project1": project_a
    ,"project2": project_b
    }


print(json.dumps(user_info_1, indent=4))