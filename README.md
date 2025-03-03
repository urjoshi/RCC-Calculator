# RCC Design Calculator

## Overview
The **RCC Design Calculator** is a Python-based tool for designing reinforced concrete beams using the **Limit State Design** method. It provides calculations for singly reinforced beams, including:
- Moment of Resistance Calculation
- Area of Reinforcement Steel Calculation
- Depth of Neutral Axis Calculation

## Features
- Calculates the **moment of resistance** of a singly reinforced beam.
- Computes the **required area of reinforcement steel** based on applied loads.
- Determines the **depth of the neutral axis**.
- Validates user inputs to ensure correct calculations.
- Provides a user-friendly command-line interface.

## Installation & Requirements
### Prerequisites
- Python 3.x installed on your system
- Basic understanding of Reinforced Concrete Design principles

### Running the Program
1. Clone or download the script.
2. Open a terminal or command prompt and navigate to the script directory.
3. Run the script using:
   ```sh
   python rcc_calculator.py
   ```
4. Follow the on-screen instructions to perform beam calculations.

## Usage
Upon running the script, the user will be prompted to choose between:
1. **Singly Reinforced Beam Design**
2. **Doubly Reinforced Beam Design** (Feature not yet implemented)

If option 1 is selected, the user can then choose:
- **Moment of Resistance Calculation**
- **Area of Reinforcement Steel Calculation**
- **Calculation of Neutral Axis Depth**

The program will request relevant input values (e.g., concrete strength, steel strength, beam dimensions) and return the calculated values.

## Example Input & Output
```
RCC DESIGN CALCULATOR

1. Singly Reinforced Beam
2. Doubly Reinforced Beam
Choose an option: 1

Welcome to the Singly Reinforced Beam Design window

1 > Moment of Resistance Calculation
2 > Area of Reinforcement Steel Calculation
3 > Calculation of Depth of Neutral Axis
Choose an option: 1

Enter the strength of Concrete to be used (N/mm^2): 25
Enter the strength of Steel (N/mm^2): 415
Enter the breadth of the beam (mm): 300
Enter the depth of the beam (mm): 500
Enter the span of the beam (mm): 6000
The maximum depth of the neutral axis is: 240.0 mm
Moment of resistance of the beam: 312500000.0 Nmm
```

## Future Enhancements
- **Doubly Reinforced Beam Calculation**
- **Shear and Deflection Analysis**
- **Graphical User Interface (GUI) Implementation**
- **Integration with Structural Design Software**

## Contributing
If you'd like to contribute to the project, feel free to fork the repository and submit pull requests with improvements or additional features.



