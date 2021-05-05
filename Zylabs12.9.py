# Aaron Oviedo 1990958


name_age = input().split()
name = name_age[0]
while name != '-1':
    try:
        age = int(name_age[1]) + 1
    except Exception as age_ex:
        age = 0
    print(name, age)
    name_age = input().split()
    name = name_age[0]
