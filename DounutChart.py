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

# Create the outer pie chart (larger)
plt.pie(values, labels=[item["name"] for item in data], autopct='%1.1f%%', startangle=90, colors=colors, explode=explode, wedgeprops=dict(width=0.3), pctdistance=0.85)

# Draw a white circle in the center to create the donut effect
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('2D Donut Chart for Data Items')
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

plt.show()
