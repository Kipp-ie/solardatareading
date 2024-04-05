import pandas as pd


df = pd.read_csv('PV-Data-22tm24.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

#start = input("Enter start  Date\n")
#end = input("Enter end  Date\n")

start = "04/02/2024 00:00"
end = "04/02/2024 23:59"

energystart = 500
energyend = 600



energy = "true"

if energy == "false":
    result = df[ (df['Date/Time'] >= start ) & (df['Date/Time'] <= end) ]
elif energy == "true":
    result = df[ (df['Energy Produced (Wh)'] >= energystart) & (df['Energy Produced (Wh)'] <= energyend) ]



print(result)

