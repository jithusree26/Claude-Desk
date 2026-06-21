# ============================================================
# UNIT CONVERTER - Built by jithusree26 with Claude
# ============================================================


# --- LENGTH CONVERSIONS ---

def mm_to_inches(mm):
    return mm / 25.4

def inches_to_mm(inches):
    return inches * 25.4

def m_to_feet(metres):
    return metres * 3.28084

def feet_to_m(feet):
    return feet / 3.28084


# --- TEMPERATURE CONVERSIONS ---

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


# --- PRESSURE CONVERSIONS ---

def psi_to_bar(psi):
    return psi * 0.0689476

def bar_to_psi(bar):
    return bar / 0.0689476


# --- HELPER FUNCTION: get a valid number from the user ---
# This is a reusable mini-machine that keeps asking until
# the user types an actual number. It never crashes.

def get_number(prompt):
    while True:
        # "while True" = keep looping forever until we get a good answer

        try:
            # "try" = attempt this. If it works, great. If not, go to "except".
            user_input = input(prompt)
            number = float(user_input)
            return number
            # "return" = hand this value back to whoever called this function
            # reaching "return" also exits the while loop automatically

        except ValueError:
            # "except ValueError" = this runs ONLY if float() failed
            # ValueError is the specific type of error that happens when
            # you try to convert "hello" into a number - it's not possible
            print(f"  '{user_input}' is not a valid number. Please try again.")


# --- HELPER FUNCTION: get a valid menu choice ---
# Same idea - keeps asking until the user picks 1 through 9

def get_choice():
    while True:
        try:
            choice = input("\nEnter a number (1-9): ").strip()
            # .strip() removes any accidental spaces the user typed
            if choice in ["1","2","3","4","5","6","7","8","9"]:
                return choice
            else:
                print("  Please enter a number between 1 and 9.")
        except:
            print("  Something went wrong. Please try again.")


# --- THE MAIN MENU ---

def main():
    print("============================================")
    print("   JITHU'S MECHANICAL ENGINEER UNIT CONVERTER")
    print("============================================")

    while True:
        print("\nWhat would you like to convert?")
        print("  1. mm       ->  inches")
        print("  2. inches   ->  mm")
        print("  3. metres   ->  feet")
        print("  4. feet     ->  metres")
        print("  5. Celsius  ->  Fahrenheit")
        print("  6. Fahrenheit  ->  Celsius")
        print("  7. PSI      ->  bar")
        print("  8. bar      ->  PSI")
        print("  9. Quit")

        choice = get_choice()
        # Notice we now call our helper function instead of raw input()
        # The helper guarantees we get a valid choice - no crash possible

        if choice == "9":
            print("\nGoodbye, Jithu!")
            break

        # Ask for the value using our safe helper function
        value = get_number("\nEnter the value: ")

        # Run the correct conversion and show the result
        if choice == "1":
            result = mm_to_inches(value)
            print(f"\n  {value} mm  =  {result:.4f} inches")

        elif choice == "2":
            result = inches_to_mm(value)
            print(f"\n  {value} inches  =  {result:.4f} mm")

        elif choice == "3":
            result = m_to_feet(value)
            print(f"\n  {value} metres  =  {result:.4f} feet")

        elif choice == "4":
            result = feet_to_m(value)
            print(f"\n  {value} feet  =  {result:.4f} metres")

        elif choice == "5":
            result = celsius_to_fahrenheit(value)
            print(f"\n  {value} °C  =  {result:.2f} °F")

        elif choice == "6":
            result = fahrenheit_to_celsius(value)
            print(f"\n  {value} °F  =  {result:.2f} °C")

        elif choice == "7":
            result = psi_to_bar(value)
            print(f"\n  {value} PSI  =  {result:.4f} bar")

        elif choice == "8":
            result = bar_to_psi(value)
            print(f"\n  {value} bar  =  {result:.4f} PSI")

        print("  ----------------------------------------")


if __name__ == "__main__":
    main()
