import seaborn as sns
import matplotlib.pyplot as plt

data = [
    [1.0, 0.8, 0.6],
    [0.8, 1.0, 0.7],
    [0.6, 0.7, 1.0]
]

sns.heatmap(data)

plt.title("Basic Heatmap")

plt.show()