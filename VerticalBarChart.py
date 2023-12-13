import matplotlib.pyplot as plt

data = [
    {"name": "Health", "value": 90, "color": "blue"},
    {"name": "Love", "value": 12, "color": "red"},
    {"name": "Family", "value": 34, "color": "green"},
    {"name": "Profession", "value": 53, "color": "yellow"},
    {"name": "Passion", "value": 98, "color": "orange"},
]

names = [item["name"] for item in data]
values = [item["value"] for item in data]
colors = [item["color"] for item in data]

plt.bar(names, values, color=colors)
plt.ylabel('Percentage')
plt.title('Vertical Bar Chart for Data Items')
plt.show()
