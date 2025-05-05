# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# Load data from CSV
data = pd.read_csv('womens_world_cup_winners.csv')

# Create a unique label for each match using Winner and Year
data['Label'] = data['Winner'] + ' (' + data['Year'].astype(str) + ')'

# the label locations
x = np.arange(len(data))  

# Set up bar positions
bar_width = 0.4

# Create the plot
plt.figure(figsize=(12, 6))

# Plot Goals Scored 
plt.bar(x - bar_width/2, data['Goals Scored'], width=bar_width, label='Goals Scored', color='skyblue')

# Plot Goals Conceded, both bars straddling their point on the x-axis
plt.bar(x + bar_width/2, data['Goals Conceded'], width=bar_width, label='Goals Conceded', color='green')

# Labels and format
plt.xlabel('Year and Winner', fontsize=12)
plt.ylabel('Goals', fontsize=12)
plt.title('Goals Scored vs Goals Conceded in Women\'s World Cup Finals (1991-2023)', fontsize=14)
plt.xticks(x, data['Label'], rotation=45, ha='right')
plt.legend()
plt.tight_layout()

# Show plot
plt.show()