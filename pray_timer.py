import pandas as pd

data = pd.read_csv('meeting_saved_chat.txt', sep='From', header=None, names=['Time','Name'], engine='python')

data['Time'] = data['Time'].map(lambda x:x.strip())
data['Time'] = pd.to_datetime(data['Time'])

n_data = data['Name'].str.split(':', expand=True)
data['Name'] = n_data[0]
data.sort_values(['Name','Time'], inplace=True)

data['Duration'] = data.groupby('Name')['Time'].diff()
data = data.dropna(subset=['Duration'])

m_data = data['Duration'].astype(str).str.split('days', expand=True)
data.loc[:,'Duration'] = m_data[1]

data_out = data[['Name','Duration']]
data_out.to_csv("prayer_time.csv", index=False)