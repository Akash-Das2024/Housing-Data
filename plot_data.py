import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    'Metro_zhvf_growth_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv')


# plot growth of to 10 states

top_10 = df[df['RegionType'] == 'msa'].sort_values('SizeRank').head(10)
growth_data = top_10[['RegionName', '2023-02-28', '2023-04-30', '2024-01-31']]
growth_data.set_index('RegionName', inplace=True)
growth_data = growth_data.T

plt.plot(growth_data)
plt.legend(growth_data.columns)
plt.title('Growth of Top 10 Cities')
plt.xlabel('Date')
plt.ylabel('Growth')
plt.show()


# doing the same for bottom 10
buttom_10 = df[df['RegionType'] == 'msa'].sort_values('SizeRank').tail(10)

growth_data = buttom_10[['RegionName',
                         '2023-02-28', '2023-04-30', '2024-01-31']]
growth_data.set_index('RegionName', inplace=True)
growth_data = growth_data.T

plt.plot(growth_data)
plt.legend(growth_data.columns)
plt.title('Growth of Top 10 Cities')
plt.xlabel('Date')
plt.ylabel('Growth')
plt.show()


# average growth of all the states over the duration of three dates
city_grouped = df[df['RegionType'] == 'msa'].groupby('RegionName').mean()
growth_data = city_grouped[['2023-02-28', '2023-04-30', '2024-01-31']]
growth_data['Avg Growth'] = growth_data.mean(axis=1)
growth_data = growth_data.sort_values('Avg Growth', ascending=False)
top_10 = growth_data.head(10)

plt.bar(top_10.index, top_10['Avg Growth'])
plt.xticks(rotation=90)
plt.title('Average Growth for Top 10 Cities')
plt.xlabel('City')
plt.ylabel('Average Growth Rate (%)')
plt.show()


# average growth over all states in a specific date
avg_growth = df[['2023-02-28', '2023-04-30', '2024-01-31']].mean()

plt.bar(avg_growth.index, avg_growth)
plt.title('Average Growth Rate for All MSAs')
plt.xlabel('Date')
plt.ylabel('Average Growth Rate (%)')
plt.show()
