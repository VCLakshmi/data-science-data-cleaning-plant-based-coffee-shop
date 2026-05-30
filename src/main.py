import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/raw/coffee-survey-results.csv")
print("People's Coffee preferences including which dairy is prefered:")
print(df)

# To get the data type of each column
print("\n\n")
print(df.info())

# To get the column names
print("\n\n")
print(df.columns)

needed_columns = [
    'What kind of dairy? (Whole milk)',
    'What kind of dairy? (Skim milk)',
    'What kind of dairy? (Half and half)',
    'What kind of dairy? (Coffee creamer)',
    'What kind of dairy? (Flavored creamer)',
    'What kind of dairy? (Oat milk)',
    'What kind of dairy? (Almond milk)',
    'What kind of dairy? (Soy milk)',
]

dairy = df[needed_columns]

# rename column names
rename_map = {
    'What kind of dairy? (Whole milk)': 'Whole milk',
    'What kind of dairy? (Skim milk)': 'Skim milk',
    'What kind of dairy? (Half and half)': 'Half and half',
    'What kind of dairy? (Coffee creamer)': 'Coffee creamer',
    'What kind of dairy? (Flavored creamer)': 'Flavored creamer',
    'What kind of dairy? (Oat milk)': 'Oat milk',
    'What kind of dairy? (Almond milk)': 'Almond milk',
    'What kind of dairy? (Soy milk)': 'Soy milk',
}

dairy = dairy.rename(columns=rename_map)
print("\nNew dataframe that shows only the dairy preferences:")
print(dairy)


# Check how many NaNs each column has.
print("\nCount of Unanswered questions: ")
print(dairy.isna().sum())


# Drop the unanswered (no data) fields.
dairy = dairy.dropna()
print("\nDataframe after removing unanswered questions:")
print(dairy)


dairy_preferences = dairy.mean() * 100
print("\nPercentage of people and their dairy preferences: ")

dairy_preferences = dairy_preferences.sort_values()
print(dairy_preferences)
dairy_preferences.to_csv("output/dairy_preferences.csv")

plt.barh(dairy_preferences.index, dairy_preferences)
plt.xlabel("Percentage of People")
plt.ylabel("Dairy Choices")
plt.title("Percentage of people preferring each dairy")
plt.savefig("output/figures/people-and-their-dairy-choices.png")
plt.show()



# identify the sweeteners that coffee shop should pile up to meet customer preferences
sweetener_field_names = [
    'What kind of sugar or sweetener? (Granulated Sugar)',
    'What kind of sugar or sweetener? (Artificial Sweetener)',
    'What kind of sugar or sweetener? (Honey)',
    'What kind of sugar or sweetener? (Maple Syrup)',
    'What kind of sugar or sweetener? (Stevia)',
    'What kind of sugar or sweetener? (Agave Nectar)',
    'What kind of sugar or sweetener? (Brown Sugar)',
    'What kind of sugar or sweetener? (Raw Sugar)',
]

sweetener_field_map = {
    'What kind of sugar or sweetener? (Granulated Sugar)': 'Granulated Sugar',
    'What kind of sugar or sweetener? (Artificial Sweetener)': 'Artificial Sweetener',
    'What kind of sugar or sweetener? (Honey)': 'Honey',
    'What kind of sugar or sweetener? (Maple Syrup)': 'Maple Syrup',
    'What kind of sugar or sweetener? (Stevia)': 'Stevia',
    'What kind of sugar or sweetener? (Agave Nectar)': 'Agave Nectar',
    'What kind of sugar or sweetener? (Brown Sugar)': 'Brown Sugar',
    'What kind of sugar or sweetener? (Raw Sugar)': 'Raw Sugar',
}

sweeteners = df[sweetener_field_names]
sweeteners = sweeteners.rename(columns=sweetener_field_map)
print("\n\nNew dataset that shows the Sweetener or sugar preferences:")
print(sweeteners)

print("\nCount of sweeteners not prefered by any:")
print(sweeteners.isna().sum())

sweeteners = sweeteners.dropna()
print("\n\nSweeteners that are preferred: ")
print(sweeteners)

# Find the percentage of sweeteners perferred.
sweeteners_choice = sweeteners.mean() * 100
print("\nPercentage of customers that prefers each sweeteners:")
print(sweeteners_choice)
sweeteners_choice.to_csv("output/sweeteners_choice.csv")

plt.barh(sweeteners_choice.index, sweeteners_choice)
plt.xlabel("Percentage of People")
plt.ylabel("Sweeteners prefered")
plt.title("Percentage of people preferring different sweeteners")
plt.savefig("output/figures/people-and-their-sweetener-choices.png")
plt.show()
