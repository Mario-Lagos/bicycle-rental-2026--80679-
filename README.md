# Bicycle Rental System

## 1. Project Overview

This project is a Bicycle Rental System developed using Python 3. It was created for the Modern Programming Principles & Practice 1 module.

The application allows users to manage bicycle rentals. It can create bicycle objects, rent and return bicycles, update rental prices, and calculate rental costs.

The project demonstrates Object-Oriented Programming (OOP), including classes, objects, inheritance, abstract classes, class methods, input validation, exception handling, and automated unit testing.

## 2. Student Information

- **Full Name:** Mario Lagos
- **Student Number:** 80679
- **Module:** Modern Programming Principles & Practice 1
- **Assessment:** CA1 – Bicycle Rental System
- **Programming Language:** Python 3

## 3. Project Files

The project contains the following files:

- `main.py`: Runs the main program and demonstrates the rental system.
- `bicycle.py`: Contains the Bicycle class and its methods.
- `rental_item.py`: Contains the abstract RentalItem class.
- `test_bicycle.py`: Contains automated unit tests.
- `README.md`: Provides project information and instructions.

## 4. Main Features

The system includes the following features:

- Creating bicycle objects with different types and prices.
- Checking bicycle availability.
- Renting available bicycles.
- Returning rented bicycles.
- Updating hourly rental prices.
- Calculating rental costs.
- Validating input data.
- Handling errors using exceptions.
- Creating bicycles using an alternative constructor.
- Testing the system using Python's unittest module.

## 5. Requirements

To run this project, you need:

- Python 3 installed on your computer.
- Visual Studio Code or another code editor.
- A terminal to run the Python commands.

No additional Python packages are required because the project uses Python's built-in `unittest` module.

## 6. How to Run the Application

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Make sure the terminal is in the project folder.
4. Run the following command:

```bash
python3 main.py
```

The program will display four bicycles and demonstrate successful and unsuccessful rental operations, rental cost calculation, price changes, input validation, and the alternative constructor.

## 7. How to Run the Tests

Open the terminal in the project folder and run:

```bash
python3 -m unittest -v test_bicycle.py
```

The tests check the main features of the system, including bicycle creation, availability, renting, returning, price management, rental cost calculation, input validation, and the abstract base class.

If all tests pass, the terminal displays `OK`.

## 8. Assumptions

The following assumptions were made during development:

- Rental prices are calculated per hour.
- Rental prices cannot be negative.
- Rental duration must be greater than zero.
- A bicycle can only be rented when it is available.
- A bicycle cannot be returned if it has not been rented.
- The standard bicycle constructor uses an hourly rental price of €10.
- Rental information is stored in the program while it is running. The application does not use a database.

## 9. AI Assistance Acknowledgement

I used ChatGPT as an AI learning assistant to help me understand the assignment requirements, Python OOP concepts, code structure, automated testing, and project documentation.

I reviewed and tested the code and used the explanations to support my understanding of the project.

## 10. Conclusion

This project demonstrates how Python OOP can be used to develop a simple Bicycle Rental System. It includes bicycle management, rental operations, input validation, exception handling, and automated tests.

The assignment helped me practise creating classes and objects, using inheritance and abstract classes, and testing a Python application.
# bicycle-rental-2026--80679-
