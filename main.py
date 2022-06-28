import csv
import pandas as pd

df = pd.read_csv("bright_stars.csv")

Mass = df['Mass']
Radius = df['Radius']

solar_radius = []
solar_mass = []

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for Mass in csvreader: 
        solar_mass.append(Mass)

with open("bright_stars.csv", "r") as f:
    csvreader = csv.reader(f)
    for Radius in csvreader: 
        solar_mass.append(Radius)

df.to_csv("unit_converted_stars.csv")



 






