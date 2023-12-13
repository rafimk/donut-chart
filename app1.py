import matplotlib.pyplot as plt

data = [
    {"name": "Health", "value": 90, "color": "blue" },
    {"name": "Love", "value": 12, "color": "red" },
    {"name": "Family", "value": 34, "color": "green"},
    {"name": "Profession", "value": 53, "color": "yellow"},
    {"name": "Passion", "value": 98, "color": "orange"},
    {"name": "Lazy", "value": 60, "color": "orange"}
]

# Set up the figure and axes in a 6x1 grid
fig, axs = plt.subplots(6, 1, figsize=(5, 20))

# Plot donut charts for each data item with specified colors
for i, item in enumerate(data):
    values = [item["value"], 100 - item["value"]]
    labels = [item["name"], ""]
    colors = [item["color"], 'lightgrey']

    axs[i].pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, wedgeprops=dict(width=0.3))
    axs[i].set(aspect="equal")
    axs[i].set_title(item["name"])

# Adjust layout
plt.tight_layout()

plt.suptitle('Donut Charts')
plt.show()
