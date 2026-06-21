# ============================================================
# UNIT CONVERTER - Built by jithusree26 with Claude
# ============================================================
# Lines starting with # are "comments" - the computer ignores
# them completely. They are notes for humans reading the code.
# ============================================================


# --- LENGTH CONVERSIONS ---

def mm_to_inches(mm):
    # "def" means "define a function". We're creating a mini-machine
    # called mm_to_inches. It takes one input: a value called "mm".
    # 1 inch = 25.4 mm, so we divide by 25.4 to go the other way.
    return mm / 25.4

def inches_to_mm(inches):
    return inches * 25.4

def m_to_feet(metres):
    # 1 metre = 3.28084 feet
    return metres * 3.28084

def feet_to_m(feet):
    return feet / 3.28084


# --- TEMPERATURE CONVERSIONS ---

def celsius_to_fahrenheit(c):
    # The standard formula: multiply by 9/5, then add 32
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


# --- PRESSURE CONVERSIONS ---

def psi_to_bar(psi):
    # 1 psi = 0.0689476 bar
    return psi * 0.0689476

def bar_to_psi(bar):
    return bar / 0.0689476


# --- THE MAIN MENU ---
# This is what the user sees when they run the program.
# "while True" means: keep showing the menu forever until the user quits.

def main():
    print("============================================")
    print("   JITHU'S MECHANICAL ENGINEER UNIT CONVERTER")
    print("============================================")

    while True:
        # Show the menu options
        print("\nWhat would you like to convert?")
        print("  1. mm  ->  inches")
        print("  2. inches  ->  mm")
        print("  3. metres  ->  feet")
        print("  4. feet  ->  metres")
        print("  5. Celsius  ->  Fahrenheit")
        print("  6. Fahrenheit  ->  Celsius")
        print("  7. PSI  ->  bar")
        print("  8. bar  ->  PSI")
        print("  9. Quit")

        # Ask the user to pick a number
        choice = input("\nEnter a number (1-9): ")

        if choice == "9":
            print("Goodbye!")
            break   # "break" exits the while loop - stops the program

        # Ask the user to type the value they want to convert
        value = float(input("Enter the value: "))
        # "float" means a number that can have decimals (like 3.14)
        # input() always gives us text, so float() converts it to a number

        # Now check what the user chose and run the right function
        if choice == "1":
            result = mm_to_inches(value)
            print(f"{value} mm  =  {result:.4f} inches")

        elif choice == "2":
            result = inches_to_mm(value)
            print(f"{value} inches  =  {result:.4f} mm")

        elif choice == "3":
            result = m_to_feet(value)
            print(f"{value} metres  =  {result:.4f} feet")

        elif choice == "4":
            result = feet_to_m(value)
            print(f"{value} feet  =  {result:.4f} metres")

        elif choice == "5":
            result = celsius_to_fahrenheit(value)
            print(f"{value} °C  =  {result:.2f} °F")

        elif choice == "6":
            result = fahrenheit_to_celsius(value)
            print(f"{value} °F  =  {result:.2f} °C")

        elif choice == "7":
            result = psi_to_bar(value)
            print(f"{value} PSI  =  {result:.4f} bar")

        elif choice == "8":
            result = bar_to_psi(value)
            print(f"{value} bar  =  {result:.4f} PSI")

        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


# This last line says: "run the main() function when this file is executed"
if __name__ == "__main__":
    main()
