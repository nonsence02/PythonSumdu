import pandas as pd
import matplotlib.pyplot as plt

data_dict = {
    'Year': [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Ukraine': [97407, 90792, 97335, 97569, 94918, 89472, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    'United States': [None, 31482, None, None, None, None, None, None, None, None, None, 231900, 52078, None, 76669, None, None, None, None, None, None]
}

data_melted = pd.DataFrame(data_dict)
data_melted.set_index('Year', inplace=True)

# Функція для побудови лінійних графіків
def plot_line_graph(country1, country2):
    plt.figure(figsize=(10, 5))
    plt.plot(data_melted.index, data_melted[country1], marker='o', label=country1)
    plt.plot(data_melted.index, data_melted[country2], marker='s', label=country2)
    plt.xlabel('Year')
    plt.ylabel('Indicator Value')
    plt.title('Indicator Dynamics')
    plt.legend()
    plt.grid(True)
    plt.show()

# Функція для побудови стовпчастої діаграми
def plot_bar_chart(country):
    plt.figure(figsize=(10, 5))
    plt.bar(data_melted.index, data_melted[country], color='skyblue')
    plt.xlabel('Year')
    plt.ylabel('Indicator Value')
    plt.title(f'Indicator Values for {country}')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

country1 = input("Enter the first country: ")
country2 = input("Enter the second country: ")

plot_line_graph(country1, country2)

country = input("Enter the country for the bar chart: ")
plot_bar_chart(country)
