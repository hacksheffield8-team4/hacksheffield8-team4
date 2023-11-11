import pandas as pd
import numpy as np

df = pd.read_csv("customerData.csv")

# Remove duplicate rows and save to new csv
df_duplicates_removed = df.drop_duplicates()
df.to_csv('customerData_new.csv', index=False, encoding='utf-8')

# Sort csv by date and time
df['Formatted_DateTime'] = pd.to_datetime(df['Date_UTC'])
df = df.sort_values(by='Formatted_DateTime')
df.to_csv('customerData_sortedByDateTime.csv', index=False)

batteryEfficiency = 0.92

numberOfPanels = 18
numberOfBatteries = 1

costOfPanels = numberOfPanels * 20
costOfBatteries = numberOfBatteries * 200

def calculateCost(loadPower, pvPower, priceOfEnergy, numberOfBatteries):
    cost = ((loadPower - pvPower) * priceOfEnergy)/4
    return cost

df['cost_for_15m'] = df.apply(lambda x: ((x['load_power_kW'] - x['pv_totalPower_kW']) * x['price_total_NZDperkWh'])/4, axis=1)
df.to_csv('customerData_with_costs.csv', index=False, encoding='utf-8')

# df['F(x)'] = df.loc[df['customerID'] == 62].mul(df['load_power_kW'], df['price_total_NZDperkWh'])
# print(df['F(x)'])
# print(df.loc[df['customerID'] == 62])
# print(calculateCost(numberOfPanels, numberOfBatteries))

# print(df.dtypes)