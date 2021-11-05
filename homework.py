import csv
import pandas as pd
import math

data = []

df = pd.read_csv('main.csv')

with open('main.csv') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data.append(i)

header = data[0]
planet_data = data[1:]

header[0] = 'row_num'
radius = df['Radius'].tolist()
mass = df['Mass'].tolist()
gravity = []
new_mass = []
new_radius = []

for index in range(1,51,2):
    r = float(radius[index]) * 6.957e+8
    new_radius.append(r)
    m = float(mass[index]) * 1.989e+30
    new_mass.append(m)
    g = (6.67 * pow(10,-11) * m) / pow(r,2)
    gravity.append(g)

new_df = pd.DataFrame({'radius' : new_radius , 'mass' : new_mass , 'gravity' : gravity})