import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Define the periodic table elements with basic information
elements = [
    {"symbol": "H", "name": "Hydrogen", "atomic_number": 1, "group": 1, "period": 1},
    {"symbol": "He", "name": "Helium", "atomic_number": 2, "group": 18, "period": 1},
    {"symbol": "Li", "name": "Lithium", "atomic_number": 3, "group": 1, "period": 2},
    {"symbol": "Be", "name": "Beryllium", "atomic_number": 4, "group": 2, "period": 2},
    {"symbol": "B", "name": "Boron", "atomic_number": 5, "group": 13, "period": 2},
    {"symbol": "C", "name": "Carbon", "atomic_number": 6, "group": 14, "period": 2},
    {"symbol": "N", "name": "Nitrogen", "atomic_number": 7, "group": 15, "period": 2},
    {"symbol": "O", "name": "Oxygen", "atomic_number": 8, "group": 16, "period": 2},
    {"symbol": "F", "name": "Fluorine", "atomic_number": 9, "group": 17, "period": 2},
    {"symbol": "Ne", "name": "Neon", "atomic_number": 10, "group": 18, "period": 2},
    # You can add more elements here for the entire periodic table
]

# Define the figure
fig, ax = plt.subplots(figsize=(15, 10))
ax.set_xlim(0, 18)
ax.set_ylim(0, 10)
ax.set_axis_off()

# Define colors for different groups
group_colors = {
    1: '#f3f4f6',
    2: '#a1c9f4',
    13: '#f4d3a1',
    14: '#f4b0a1',
    15: '#f4a1c4',
    16: '#a1f4a8',
    17: '#c1f4a1',
    18: '#a1f4e4'
}

# Plot each element
for element in elements:
    group = element["group"]
    period = element["period"]
    symbol = element["symbol"]
    atomic_number = element["atomic_number"]

    # Determine color by group
    color = group_colors.get(group, '#ffffff')

    # Add a rectangle for the element
    rect = Rectangle((group - 1, 10 - period), 1, 1, edgecolor='black', facecolor=color)
    ax.add_patch(rect)

    # Add the element's symbol and atomic number
    ax.text(group - 0.5, 10 - period + 0.5, symbol, va='center', ha='center', fontsize=12, weight='bold')
    ax.text(group - 0.5, 10 - period + 0.2, str(atomic_number), va='center', ha='center', fontsize=8)

# Set title
plt.title("Periodic Table of Elements", fontsize=16)

# Show the periodic table
plt.show()
