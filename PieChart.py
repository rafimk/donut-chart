import matplotlib.pyplot as plt

data = [
    {"name": "Health", "value": 90, "color": "blue" },
    {"name": "Love", "value": 12, "color": "red" },
    {"name": "Family", "value": 34, "color": "green"},
    {"name": "Profession", "value": 53, "color": "yellow"},
    {"name": "Passion", "value": 98, "color": "orange"},
]

colors = [item["color"] for item in data]
values = [item["value"] for item in data]
explode = [0.1] * len(data)  # To create some separation

plt.pie(values, labels=[item["name"] for item in data], autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, shadow=True)
plt.title('2D Pie Chart for Data Items')
plt.show()
