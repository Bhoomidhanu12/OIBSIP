def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal weight"
    elif 25 <= bmi < 29.9:
        return "overweight"
    else:
        return "obese"

def main():
    weight = int(input("Enter your weight (in kilograms): "))
    height = int(input("Enter your height (in meters): "))

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as {category}.")

if __name__ == "__main__":
    main()
