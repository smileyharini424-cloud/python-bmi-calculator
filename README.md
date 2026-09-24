# BMI Calculator

## Explanation

The BMI Calculator is a Python program that calculates Body Mass Index (BMI) using a person's weight and height.

## Problem Statement

Create a Python program that accepts weight in kilograms and height in meters, calculates BMI, and displays the corresponding BMI category.

## Features

* Accepts weight and height
* Calculates BMI
* Displays BMI value
* Determines BMI category
* Handles invalid input

## How It Works

1. Enter weight in kilograms.
2. Enter height in meters.
3. Calculate BMI using the formula:

   `BMI = weight / (height × height)`
4. Determine the BMI category.
5. Display the result.

## BMI Categories

| BMI Range     | Category    |
| ------------- | ----------- |
| Below 18.5    | Underweight |
| 18.5 - 24.9   | Normal      |
| 25.0 - 29.9   | Overweight  |
| 30.0 or above | Obesity     |

## Technologies Used

* Python
* Functions
* Conditional Statements
* Exception Handling

## Data Structure Used

* No special data structure

## Methods Used

* `calculate_bmi()`
* `get_category()`
* `main()`

## Program Flow

```text
Start
  ↓
Enter Weight
  ↓
Enter Height
  ↓
Calculate BMI
  ↓
Determine Category
  ↓
Display Result
  ↓
End
```

## Sample Input

```text
Enter weight in kg: 60
Enter height in meters: 1.65
```

## Sample Output

```text
BMI = 22.04
Category = Normal
```

## Time Complexity

O(1)

## Space Complexity

O(1)

## Key Learning

* Creating functions
* Performing mathematical calculations
* Using conditional statements
* Validating user input
* Building a simple Python application

## File Location

`bmi_calculator.py`

## Repository Structure

```text
python-bmi-calculator/
│
├── bmi_calculator.py
└── README.md
```

## Author

V.Harini
