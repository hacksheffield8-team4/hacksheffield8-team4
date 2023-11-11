import pandas as pd
import numpy as np

df = pd.read_csv("customerData.csv")

# Remove duplicate rows and save to new csv
df_duplicates_removed = df.drop_duplicates()
df.to_csv('customerData_new.csv', index=False, encoding='utf-8')

batteryEfficiency = 0.92

numberOfPanels = 18
numberOfBatteries = 1

def calculateCost(numberOfPanels, numberOfBatteries):
    batteryCost = 3000
    panelCost = 200
    cost = numberOfBatteries * batteryCost + numberOfPanels * panelCost
    
    return cost

df['F(x)'] = df.loc[df['customerID'] == 62].mul(df['load_power_kW'], df['price_total_NZDperkWh'])
print(df['F(x)'])
print(df.loc[df['customerID'] == 62])
print(calculateCost(numberOfPanels, numberOfBatteries))

print(df.dtypes)