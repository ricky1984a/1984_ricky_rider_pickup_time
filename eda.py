# Import necessary libraries
import pandas as pd  # Used for data manipulation and analysis
import seaborn as sns  # High-level interface for drawing statistical graphics
import matplotlib.pyplot as plt  # Used for creating static, interactive, and animated visualizations

# Read the CSV file and load it into a pandas DataFrame
df = pd.read_csv('uber_pickups.csv')  # Replace 'uber_pickups.csv' with the actual file path
print(df.head())  # Display the first 5 rows of the dataset

# Clean the data by dropping missing values
df.dropna(inplace=True)  # Removes rows that contain missing values and modifies the DataFrame directly

# Convert pickup datetime to a usable format
df['pickup_time'] = pd.to_datetime(df['pickup_time'])  # Ensure the column name matches the dataset

# Extract the hour from the pickup time for analysis
df['hour'] = df['pickup_time'].dt.hour  # Extract the hour from each timestamp in the 'pickup_time' column


# Create a histogram to visualize the distribution of pickups by hour
sns.histplot(df['hour'], bins=24, kde=False)  # Create a histogram using the 'hour' column
plt.title('Distribution of Uber Pickups by Hour')  # Set the title
plt.xlabel('Hour of the Day')  # Label x-axis as "Hour of the Day"
plt.ylabel('Number of Pickups')  # Label y-axis as "Number of Pickups"
plt.show()  # Display the histogram

# Create a scatter plot to visualize the relationship between pickup time and number of rides
plt.scatter(df['hour'], df['number_of_rides'])  # Create a scatter plot where each point represents a specific hour and the corresponding number of rides
plt.title('Scatter Plot of Hour vs Number of Uber Rides')  # Set the title
plt.xlabel('Hour of the Day')  # Label x-axis as "Hour of the Day"
plt.ylabel('Number of Rides')  # Label y-axis as "Number of Rides"
plt.show()  # Display the scatter plot

