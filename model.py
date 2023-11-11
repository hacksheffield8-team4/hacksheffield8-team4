import mmap
import pandas as pd
import numpy as np

df = pd.read_csv("customerData.csv")

# Remove duplicate rows and save to new csv
df_duplicates_removed = df.drop_duplicates()

# Choose a specific customer by ID
customerID = 25
df = df.loc[df['customerID'] == customerID]

# Sort csv by date and time
df['Formatted_DateTime'] = pd.to_datetime(df['Date_UTC'])
df = df.sort_values(by='Formatted_DateTime')

batteryEfficiency = 0.92

numberOfPanels = 12
numberOfBatteries = 1

costOfPanels = numberOfPanels * 90
costOfBatteries = numberOfBatteries * 200

#def calculateCost(loadPower, pvPower, priceOfEnergy, numberOfBatteries):
#    cost = ((loadPower - pvPower) * priceOfEnergy)/4
#    return cost

# Adds column to DataFrame with cost for each 15 minute interval
df['cost_for_15m'] = df.apply(lambda x: 
                              ((x['load_power_kW'] -((x['pv_totalPower_kW']/x['NumberOfPanels'])*numberOfPanels) * x['price_gridImport_NZDperkWh'])/4) 
                              if (x['load_power_kW'] - (x['pv_totalPower_kW']/x['NumberOfPanels'])*numberOfPanels > 0)
else ((x['load_power_kW'] -((x['pv_totalPower_kW']/x['NumberOfPanels'])*numberOfPanels) * x['price_gridExport_NZDperkWh'])/4), axis=1)

df['energy_for_15m'] = df.apply(lambda x: ((x['pv_totalPower_kW']/x['NumberOfPanels'])*numberOfPanels)/4, axis=1)

# Produces csv with final DataFrame
df.to_csv('customerData_modified.csv', index=False, encoding='utf-8')

# Prints total cost for one year
print('Total cost after export: ', (costOfPanels + df['cost_for_15m'].sum()))
print('Power consumed: ', ((df['load_power_kW'].sum())/4))
print('Power generated: ', (df['energy_for_15m'].sum()))
print('Total cost before solar: ', ())

# df['F(x)'] = df.loc[df['customerID'] == 62].mul(df['load_power_kW'], df['price_total_NZDperkWh'])
# print(df['F(x)'])
# print(df.loc[df['customerID'] == 62])
# print(calculateCost(numberOfPanels, numberOfBatteries))

# print(df.dtypes)