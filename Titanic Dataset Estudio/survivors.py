import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

df = pd.read_csv("kaggle/titanic/train.csv")


def cleaning_data(df):
    # Remove unwanted columns
    df = df.drop(columns=["PassengerId", "Pclass", "Name", "Sex", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"])

    # Fill all the null values with the median of Age colum
    mediana_edad = df["Age"].median()
    df["Age"] = df["Age"].fillna(mediana_edad)
    df["Age"] = df["Age"].map(lambda age: int(age))
    df["Age"] = df["Age"].map(lambda age: int(mediana_edad) if age < 3 else age)

    return df


# Data cleaning and preprocessing 
df = cleaning_data(df)

# Filt Data to Plot
datos_completos = df["Survived"]

survivors = df[df["Survived"] == 1]["Age"]

not_survivors = df[df["Survived"] == 0]["Age"]

# Define bins (from 0 - 80 years old into ranges / steps of 10-10)
bins_edades = range(0, 85, 10)

plt.hist(
    [survivors, not_survivors], 
    bins=bins_edades,          
    color=['tab:green', 'tab:red'],        # first color for survivors, second color for not survivors
    label=['Survivors', 'Not Survivors']
)


plt.xlabel("Ages", fontdict={'family': 'serif', 'size': 14})
plt.ylabel("Amount of People", fontdict={'family': 'serif', 'size': 14})
plt.legend(prop={'family': 'serif', 'size': 10})
plt.title("Titanic Survivors / Not Survivors", fontdict={'family': 'serif', 'size': 14})

plt.show()

tothirdty = survivors[(survivors >= 20) & (survivors < 30)]
tofourty = survivors[(survivors >= 30) & (survivors < 40)]
tofifty = survivors[(survivors >= 40) & (survivors < 50)]

tothirdty_nots = not_survivors[(not_survivors >= 20) & (not_survivors < 30)]
tofourty_nots = not_survivors[(not_survivors >= 30) & (not_survivors < 40)]
tofifty_nots = not_survivors[(not_survivors >= 40) & (not_survivors < 50)]

print(f"There are {len(tothirdty)} surviving people aged 20 to 30")
print(f"There are {len(tofourty)} surviving people aged 30 to 40")
print(f"There are {len(tofifty)} surviving people aged 40 to 50")

print("..........................................................")
print(f"There are {len(tothirdty_nots)} dead people aged 20 to 30")
print(f"There are {len(tofourty_nots)} dead people aged 30 to 40")
print(f"There are {len(tofifty_nots)} dead people aged 40 to 50")

