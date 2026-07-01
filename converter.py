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


# --- HELPER: get a valid number from the user ---

def get_number(prompt):
    while True:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            print(f"  '{user_input}' is not a valid number. Please try again.")


# --- HELPER: get a valid menu choice ---

def get_choice():
    while True:
        try:
            choice = input("\nEnter a number (1-9): ").strip()
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

    # This is our history list - starts empty, like a blank notepad
    # Every conversion we do gets written onto this notepad
    history = []

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
        print("  9. Quit and show history")

        choice = get_choice()

        if choice == "9":
            # Show the history before quitting
            print("\n============================================")
            print("   SESSION HISTORY")
            print("============================================")

            if len(history) == 0:
                # len() means "how many items are in this list?"
                # len([]) = 0, len([1,2,3]) = 3
                print("  No conversions done this session.")
            else:
                # for loop: go through history list, one entry at a time
                # "i" is a counter - tells us which number entry we're on
                # enumerate() gives us both the position number AND the value
                for i, entry in enumerate(history, start=1):
                    print(f"  {i}. {entry}")

            print("============================================")
            print("\nGoodbye, Jithu!")
            break

        value = get_number("\nEnter the value: ")

        # Do the conversion and build the result text
        if choice == "1":
            result = mm_to_inches(value)
            entry = f"{value} mm  =  {result:.4f} inches"

        elif choice == "2":
            result = inches_to_mm(value)
            entry = f"{value} inches  =  {result:.4f} mm"

        elif choice == "3":
            result = m_to_feet(value)
            entry = f"{value} metres  =  {result:.4f} feet"

        elif choice == "4":
            result = feet_to_m(value)
            entry = f"{value} feet  =  {result:.4f} metres"

        elif choice == "5":
            result = celsius_to_fahrenheit(value)
            entry = f"{value} °C  =  {result:.2f} °F"

        elif choice == "6":
            result = fahrenheit_to_celsius(value)
            entry = f"{value} °F  =  {result:.2f} °C"

        elif choice == "7":
            result = psi_to_bar(value)
            entry = f"{value} PSI  =  {result:.4f} bar"

        elif choice == "8":
            result = bar_to_psi(value)
            entry = f"{value} bar  =  {result:.4f} PSI"

        # Show the result on screen
        print(f"\n  {entry}")
        print("  ----------------------------------------")

        # Add this conversion to the history list
        # Like writing the result on the next line of your notepad
        history.append(entry)


if __name__ == "__main__":
    main()
