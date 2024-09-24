import pandas as pd
data = {
    'date': ['2023-09-01', '2023-09-02', 'invalid_date', '2023-09-04'],
    'value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

try:
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
except ValueError as e:
    raise ValueError("Date must be in YYYY-MM-DD format") 
print(df)