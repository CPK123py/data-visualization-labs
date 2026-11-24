import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(42)
locations = ['Mg road', 'Koramangala', 'Silkboard', 'Brigade Road', 'Whitefield']
dates = pd.date_range('2024-10-01', periods=50)
data = []

for date in dates:
    for loc in locations:
        data.append({
            'location': loc,
            'date': date.strftime('%Y-%m-%d'),
            'time': f"{np.random.randint(0, 24):02d}:00",
            'vehicle_count': np.random.randint(200, 1800),
            'accident_count': np.random.randint(0, 2),
            'dominant_vehicle': np.random.choice(['car', 'Truck', 'Auto', 'Bus'])
        })

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
print("data.csv created")

# Create 5 simple plots
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
fig.suptitle('Smart City Traffic Analysis', fontsize=14, fontweight='bold')

# 1. Heatmap
ax = axes[0, 0]
heat = df.pivot_table(values='vehicle_count', index='location', columns='dominant_vehicle', aggfunc='mean')
im = ax.imshow(heat.values, cmap='YlOrRd')
ax.set_xticks(range(len(heat.columns)))
ax.set_yticks(range(len(heat.index)))
ax.set_xticklabels(heat.columns, rotation=45)
ax.set_yticklabels(heat.index)
ax.set_title('Heatmap: Vehicles by Location')
plt.colorbar(im, ax=ax)

#Dashboard implementation 
# 2. Bar chart 
ax = axes[0, 1]
loc_avg = df.groupby('location')['vehicle_count'].mean()
ax.bar(loc_avg.index, loc_avg.values, color='steelblue')
ax.set_title('Avg Vehicles by Location')
ax.tick_params(axis='x', rotation=45)

ax = axes[0, 2]
daily = df.groupby('date')['vehicle_count'].mean()
ax.plot(range(len(daily)), daily.values, marker='o', color='green')
ax.set_title('Traffic Over Time')
ax.set_xlabel('Days')

ax = axes[1, 0]
vehicle_counts = df['dominant_vehicle'].value_counts()
ax.pie(vehicle_counts.values, labels=vehicle_counts.index, autopct='%1.1f%%')
ax.set_title('Vehicle Type Distribution')

ax = axes[1, 1]
ax.scatter(df['vehicle_count'], df['accident_count'], alpha=0.6, color='red')
ax.set_title('Vehicles vs Accidents')
ax.set_xlabel('Vehicle Count')
ax.set_ylabel('Accidents')
axes[1, 2].remove()

plt.tight_layout()
plt.savefig('traffic_plots.png', dpi=150, bbox_inches='tight')
print(" traffic_plots.png saved")
plt.show()

print(f"\nDataset: {len(df)} records")
print(f"Locations: {df['location'].nunique()}")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")
