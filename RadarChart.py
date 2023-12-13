import matplotlib.pyplot as plt
import numpy as np

data = [
    {"name": "Health", "value": 90, "color": "blue"},
    {"name": "Love", "value": 12, "color": "red"},
    {"name": "Family", "value": 34, "color": "green"},
    {"name": "Profession", "value": 53, "color": "yellow"},
    {"name": "Passion", "value": 98, "color": "orange"},
]

categories = [item["name"] for item in data]
values = [item["value"] for item in data]
colors = [item["color"] for item in data]

angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color=colors, alpha=0.25)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)
plt.title('Radar Chart for Data Items')
plt.show()
