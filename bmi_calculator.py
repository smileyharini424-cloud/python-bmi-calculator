def calculate_bmi(weight, height):
    return weight / (height * height)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def main():
    print("===== BMI CALCULATOR =====")

    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters: "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be greater than zero.")
            return

        bmi = calculate_bmi(weight, height)
        category = get_category(bmi)

        print("\n===== BMI RESULT =====")
        print(f"BMI = {bmi:.2f}")
        print(f"Category = {category}")

    except ValueError:
        print("Please enter valid numeric values.")


if __name__ == "__main__":
    main()
