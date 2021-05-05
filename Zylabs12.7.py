# Aaron Oviedo 1990958

def get_age():
    age = int(input())
    if age < 18 or age > 75:
        raise ValueError("Invalid age.")
    return age


def fat_burning_heart_rate(age):
    rate = 220 - age
    rate *= 0.7
    return rate

if __name__ == "__main__":
    try:
        age = get_age()
        rate = fat_burning_heart_rate(age)
        print("Fat burning heart rate for a", age, "year-old:", rate, "bpm")
    except ValueError as val_err:
        print(val_err)
        print("Could not calculate heart rate info.\n")
