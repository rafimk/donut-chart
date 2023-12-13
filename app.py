import matplotlib.pyplot as plt

# Data
data = [
    {"name": "Health", "value": 90},
    {"name": "Love", "value": 12},
    {"name": "Family", "value": 34},
    {"name": "Profession", "value": 53},
    {"name": "Passion", "value": 98},
]

# Extracting names and values
names = [entry["name"] for entry in data]
values = [entry["value"] for entry in data]

# Create a donut chart
fig, ax = plt.subplots()

# Draw a pie chart
wedges, texts, autotexts = ax.pie(
    values,
    labels=names,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops=dict(width=0.4),
)

# Adding a circle in the center to create a donut chart
centre_circle = plt.Circle((0, 0), 0.2, color="white", edgecolor="black", linewidth=0.8, fill=False)
ax.add_artist(centre_circle)

# Equal aspect ratio ensures that the pie is drawn as a circle
ax.axis("equal")

plt.title("Donut Chart")

# Show the plot
plt.show()
