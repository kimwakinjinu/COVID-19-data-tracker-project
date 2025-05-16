import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')


# Load data
try:
    df = pd.read_csv('owid-covid-data.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: owid-covid-data.csv not found. Please make sure the file is in the correct directory.")
    # In a real notebook, you might stop here or provide instructions to upload/locate the file.
    # For this script, we'll assume the file will be available when executed.
    # If running this code, ensure the CSV is in the same directory or provide the full path.


# Check columns
print("\nColumns in the dataset:")
print(df.columns.tolist()) #

# Preview rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Identify missing values
print("\nMissing values per column (first 20 columns):")
print(df.isnull().sum().head(20))


# Filter countries of interest
countries_of_interest = ['Kenya', 'United States', 'India'] 
df_filtered = df[df['location'].isin(countries_of_interest)].copy()
print(f"\nData filtered for: {countries_of_interest}")

# Drop rows with missing dates or critical values (location, date, total_cases)
# total_cases is chosen as a critical value for basic case tracking
df_cleaned = df_filtered.dropna(subset=['date', 'location', 'total_cases']).copy()
print(f"Rows before dropping missing critical values: {len(df_filtered)}")
print(f"Rows after dropping missing critical values: {len(df_cleaned)}")


# Convert date column to datetime
df_cleaned['date'] = pd.to_datetime(df_cleaned['date'])
print("\n'date' column converted to datetime.")

# Sort data by location and date - important for ffill
df_cleaned = df_cleaned.sort_values(by=['location', 'date'])

# Handle missing numeric values
cumulative_cols = ['total_cases', 'total_deaths', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']
for col in cumulative_cols:
    if col in df_cleaned.columns:
        df_cleaned[col] = df_cleaned.groupby('location')[col].ffill()
        df_cleaned[col] = df_cleaned[col].fillna(0) 

# For daily new cases/deaths, fillna(0) is safer
daily_cols = ['new_cases', 'new_deaths', 'new_vaccinations']
for col in daily_cols:
     if col in df_cleaned.columns:
        df_cleaned[col] = df_cleaned.groupby('location')[col].fillna(0)


print("\nMissing values after cleaning (first 20 columns):")
print(df_cleaned.isnull().sum().head(20))

# Plot total cases over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_cleaned, x='date', y='total_cases', hue='location')
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Plot total deaths over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_cleaned, x='date', y='total_deaths', hue='location')
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Compare daily new cases between countries
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_cleaned, x='date', y='new_cases', hue='location')
plt.title('Daily New COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Daily New Cases')
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# Calculate the death rate
# Avoid division by zero for locations with 0 total_cases
df_cleaned['death_rate'] = (df_cleaned['total_deaths'] / df_cleaned['total_cases']).replace([float('inf'), -float('inf')], 0).fillna(0) * 100
print("\n'death_rate' calculated (Total Deaths / Total Cases * 100).")

# Display death rate for the latest date for each country
latest_data = df_cleaned.loc[df_cleaned.groupby('location')['date'].idxmax()]
print("\nLatest Death Rate (%) per country:")
print(latest_data[['location', 'date', 'death_rate']])


# Check if vaccination data exists
if 'total_vaccinations' in df_cleaned.columns and df_cleaned['total_vaccinations'].sum() > 0:
    # Plot cumulative vaccinations over time
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_cleaned, x='date', y='total_vaccinations', hue='location')
    plt.title('Cumulative COVID-19 Vaccinations Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Vaccinations')
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

    # Compare % vaccinated population (requires 'population' and 'people_vaccinated')
    if 'people_vaccinated' in df_cleaned.columns and 'population' in df_cleaned.columns:
        # Calculate percentage of population vaccinated
        df_cleaned['percent_vaccinated'] = (df_cleaned['people_vaccinated'] / df_cleaned['population']).replace([float('inf'), -float('inf')], 0).fillna(0) * 100

        # Plot percentage vaccinated over time
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df_cleaned, x='date', y='percent_vaccinated', hue='location')
        plt.title('Percentage of Population Vaccinated Over Time')
        plt.xlabel('Date')
        plt.ylabel('Percentage Vaccinated (%)')
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        plt.show()

        # Display latest percentage vaccinated
        latest_vaccination_data = df_cleaned.loc[df_cleaned.groupby('location')['date'].idxmax()]
        print("\nLatest Percentage of Population Vaccinated per country:")
        print(latest_vaccination_data[['location', 'date', 'percent_vaccinated']])

    else:
        print("\n'people_vaccinated' or 'population' column not found for calculating percentage vaccinated for the selected countries.")

else:
    print("\n'total_vaccinations' column not found or contains no vaccination data for the selected countries.")

