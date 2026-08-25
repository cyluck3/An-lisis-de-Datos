import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv("kaggle/titanic/train.csv")


def cleaning_data(df):
    # Remove unwanted columns
    df = df.drop(columns=["PassengerId", "Pclass", "Name", "SibSp", "Parch", "Ticket", "Fare", "Cabin", "Embarked"])

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
survivors_by_age = df[df["Survived"] == 1]["Age"]
not_survivors_by_age = df[df["Survived"] == 0]["Age"]

survivors_by_sex = df[df["Survived"] == 1]["Sex"].map(lambda item: 1 if item == "female" else 0)
not_survivors_by_sex = df[df["Survived"] == 0]["Sex"].map(lambda item: 1 if item == "female" else 0)

sbs_male = survivors_by_sex[survivors_by_sex == 0]
sbs_female = survivors_by_sex[survivors_by_sex == 1]
nsbs_male = not_survivors_by_sex[not_survivors_by_sex == 0]
nsbs_female = not_survivors_by_sex[not_survivors_by_sex == 1]

print(len(sbs_male), len(sbs_female), len(nsbs_male), len(nsbs_female))

# Define bins (from 0 - 80 years old into ranges / steps of 10-10)
bins_edades = range(0, 85, 10)

plt.hist(
    [survivors_by_age, not_survivors_by_age], 
    bins=bins_edades,          
    color=['tab:green', 'tab:red'],        # first color for survivors_by_age, second color for not survivors_by_age
    label=['Survivors_by_age', 'Not Survivors_by_age']
)


plt.axhline(
    y=len(sbs_male),
    color="tab:blue",
    linestyle="--",
    linewidth=2,
    label="Male Survivors",
)
plt.axhline(
    y=len(sbs_female),
    color="tab:pink",
    linestyle="dashed",   
    linewidth=2,
    label="Female Survivors",
)

plt.axhline(
    y=len(nsbs_male),
    color="red",
    linestyle="dashed",
    linewidth=2,
    label="Male Dead",
)

plt.axhline(
    y=len(nsbs_female),
    color="red",
    linestyle=":",
    linewidth=3,
    label="Female Dead",
)


plt.xlabel("Ages", fontdict={'family': 'serif', 'size': 14})
plt.ylabel("Amount of People", fontdict={'family': 'serif', 'size': 14})
plt.legend(prop={'family': 'serif', 'size': 10})
plt.title("Titanic Survivors / Not Survivors", fontdict={'family': 'serif', 'size': 14})

plt.show()

tothirdty = survivors_by_age[(survivors_by_age >= 20) & (survivors_by_age < 30)]
tofourty = survivors_by_age[(survivors_by_age >= 30) & (survivors_by_age < 40)]
tofifty = survivors_by_age[(survivors_by_age >= 40) & (survivors_by_age < 50)]

tothirdty_nots = not_survivors_by_age[(not_survivors_by_age >= 20) & (not_survivors_by_age < 30)]
tofourty_nots = not_survivors_by_age[(not_survivors_by_age >= 30) & (not_survivors_by_age < 40)]
tofifty_nots = not_survivors_by_age[(not_survivors_by_age >= 40) & (not_survivors_by_age < 50)]

print(f"There are {len(tothirdty)} surviving people aged 20 to 30")
print(f"There are {len(tofourty)} surviving people aged 30 to 40")
print(f"There are {len(tofifty)} surviving people aged 40 to 50")

print("..........................................................")
print(f"There are {len(tothirdty_nots)} dead people aged 20 to 30")
print(f"There are {len(tofourty_nots)} dead people aged 30 to 40")
print(f"There are {len(tofifty_nots)} dead people aged 40 to 50")

