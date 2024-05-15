import pandas as pd
import matplotlib.pyplot as plt


# Читання даних з CSV-файлу
def read_data_from_csv(file_path):
    try:
        df = pd.read_csv(file_path, parse_dates=['Date'], dayfirst=True)
        return df
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


# Функція для визначення найбільш популярного місяця
def get_most_popular_month(df):
    df['Month'] = df['Date'].dt.month
    df['Total'] = df.iloc[:, 2:].sum(axis=1)  # Сума всіх колонок, починаючи з третьої
    monthly_usage = df.groupby('Month')['Total'].sum().reset_index()
    most_popular_month = monthly_usage.loc[monthly_usage['Total'].idxmax()]
    return most_popular_month


# Функція для побудови графіків
def plot_data(df):
    df['Month'] = df['Date'].dt.month
    df['Total'] = df.iloc[:, 2:].sum(axis=1)
    monthly_usage = df.groupby('Month')['Total'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.bar(monthly_usage['Month'], monthly_usage['Total'], color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Total Usage')
    plt.title('Monthly Bicycle Usage in 2017')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.show()


def main():
    file_path = 'bike_usage_2017.csv'
    df = read_data_from_csv(file_path)
    if df is not None:
        most_popular_month = get_most_popular_month(df)
        print("Most popular month for cyclists in 2017:")
        print(f"Month: {most_popular_month['Month']}, Usage: {most_popular_month['Total']}")
        plot_data(df)


if __name__ == "__main__":
    main()
