def singly_reinforced():
    print('Design of a Singly Reinforced Concrete Beam using Limit State Design')

    def moment_calculation():
        M_mix = int(input("Enter the strength of Concrete to be used (N/mm^2): "))
        S_str = int(input("Enter the strength of Steel (N/mm^2): "))
        b = int(input("Enter the breadth of the beam (mm): "))
        d = int(input("Enter the depth of the beam (mm): "))
        l = int(input("Enter the span of the beam (mm): "))

        if S_str == 415:
            x_max = 0.48 * d
        elif S_str == 250:
            x_max = 0.53 * d
        else:
            x_max = 0.46 * d
        
        print(f"The maximum depth of the neutral axis is: {x_max:.2f} mm")

        M = 0.36 * M_mix * b * x_max * (d - (0.42 * x_max))
        print(f"Moment of resistance of the beam: {M:.2f} Nmm")

    def area_calculation():
        M_mix = int(input("Enter the strength of Concrete to be used (N/mm^2): "))
        S_str = int(input("Enter the strength of Steel (N/mm^2): "))
        b = int(input("Enter the breadth of the beam (mm): "))
        d = int(input("Enter the depth of the beam (mm): "))
        l = int(input("Enter the span of the beam (mm): "))
        D_Load = float(input("Enter Dead Load (N/mm^2): "))
        L_Load = float(input("Enter Live Load (N/mm^2): "))

        S_w = d * 25  # Self-weight calculation
        print(f"Self-weight of the beam: {S_w:.2f} N/mm^2")

        M = ((D_Load + L_Load) * l * l + S_w) / 8
        factored_M = 1.5 * M
        print(f"Moment: {M:.2f} Nmm")
        print(f"Factored Moment = 1.5 * Moment = {factored_M:.2f} Nmm")

        if S_str == 415:
            x_max = 0.48 * d
        elif S_str == 250:
            x_max = 0.53 * d
        else:
            x_max = 0.46 * d
        
        print(f"The maximum depth of the neutral axis is: {x_max:.2f} mm")

    def neutral_axis():
        d = float(input("Enter the diameter of the bars (mm): "))
        n1 = int(input("Enter the number of bars: "))
        Area = (3.14 * d**2 * n1) / 4
        print(f"Area of reinforcement steel: {Area:.2f} mm²")

        f = input("Are there additional bars? (Y/N): ").strip().upper()
        if f == 'Y':
            d2 = float(input("Enter the diameter of additional bars (mm): "))
            n2 = int(input("Enter the number of additional bars: "))
            A = (3.14 * d2**2 * n2) / 4
            print(f"Additional reinforcement area: {A:.2f} mm²")

    print('''
    1 > Moment of Resistance Calculation
    2 > Area of Reinforcement Steel Calculation
    3 > Calculation of Depth of Neutral Axis
    ''')
    
    try:
        answer = int(input("Choose an option: "))
        if answer == 1:
            moment_calculation()
        elif answer == 2:
            area_calculation()
        elif answer == 3:
            neutral_axis()
        else:
            print("Invalid input! Please enter a valid choice.")
    except ValueError:
        print("Invalid input! Please enter a number.")

print("RCC DESIGN CALCULATOR")
print('''
1. Singly Reinforced Beam
2. Doubly Reinforced Beam
''')

try:
    a = int(input("Choose an option: "))
    if a == 1:
        print('Welcome to the Singly Reinforced Beam Design window')
        singly_reinforced()
    elif a == 2:
        print('Welcome to the Doubly Reinforced Beam Design window (Feature not implemented yet)')
    else:
        print("Invalid input, please enter 1 or 2.")
except ValueError:
    print("Invalid input! Please enter a number.")
