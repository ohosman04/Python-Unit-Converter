def m_to_feet(meters):
    return meters * 3.28084
def feet_to_m(feet):
    return feet * 0.3048
def km_to_mile(km):
    return km * 0.621371
def mile_to_km(mile):
    return mile * 1.60934
def kg_to_lbs(kg):
    return kg * 2.20462
def lbs_to_kg(lbs):
    return lbs * 0.453592
def f_to_c(f):
    c = ((f-32) * 5/9)
    return c
def c_to_f(c):
    f = (c * 9/5) + 32
    return f
def main():
    i = 1
    while i > 0:
        try:
            value = float(input("Enter your value (without unit): ")) #possible value error
            unit = input("What is your unit of measurement (m,feet,mi,km,kg,lbs,f,c): ").lower() #possible logic error
            if unit in ['m','feet','mi','km','kg','lbs','f','c']: #catches logic error
                if unit == 'm':
                    print(f"{value} meters are {m_to_feet(value):.1f} feet!")
                if unit == 'feet':
                    print(f"{value} feet are {feet_to_m(value):.1f} meters!")
                if unit == 'mi':
                    print(f"{value} miles are {mile_to_km(value):.1f} KM!")
                if unit == 'km':
                    print(f"{value} KMs are {km_to_mile(value):.1f} miles!")
                if unit == 'kg':
                    print(f"{value} KGs are {kg_to_lbs(value):.1f} LBS!")
                if unit == 'lbs':
                    print(f"{value} LBS are {lbs_to_kg(value):.1f} KGs!")
                if unit == 'f':
                    print(f"{value}°F is {f_to_c(value):.1f}°C!")
                if unit == 'c':
                    print(f"{value}°C is {c_to_f(value):.1f}°F!")
            else:
                print("Wrong unit selection. Try again.")
            wow = 1
            while wow > 0:
                again = input("Would you like to convert again? (Y/N): ").lower() #possible logic error
                if again in ['y','n']: #catches logic error
                    if again == 'n':
                        wow = 0
                        break
                    else:
                        wow = 0
                        i = 1    
                else:
                    print("Invalid input. Try again.")
                    wow = 1
        except ValueError: #catches value error in initial input
            print("Wrong value input. Try Again.")
            return False

if __name__ == "__main__":
    print("Welcome to the Unit Converter!")
    print("Here are the conversions we can offer...")
    options = [
    'Meters -> feet',
    'Feet -> meters',
    'KM -> Miles',
    'Miles -> KM',
    'KG -> LBS',
    'LBS -> KG',
    'f -> c',
    'c -> f'
    ]
    for index,option in enumerate(options):
        print(f"{index + 1}. {option}")
    main()
    if main() == False:
        main()
    