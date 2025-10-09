# OOP_Health_Project
Health Tracker – a console-based system for monitoring your overall health condition,
including tracking weight, nutrition, physical activity, sleep, medicine, and water balance.
The system implements the Facade design pattern, which provides the user with a clear and simple interface for interacting with all health modules.

Project Architecture

src directory
The src directory contains the main interface of the program.
It includes a dedicated interfaces folder with a facade.py file implementing the Facade pattern.
The core classes are also implemented in this directory, each placed in separate subdirectories according to their function (e.g., weight, nutrition, activity, etc.).
The main entry point of the application — main.py — is also located in the src directory.

In addition to the src directory, there is a tests directory that contains separate folders for testing each individual class and component.

Technologies Used

Python 3.13, Black (code formatting), Unit Tests, Facade Pattern

