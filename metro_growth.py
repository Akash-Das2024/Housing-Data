import pandas as pd

df = pd.read_csv(
    'Metro_zhvf_growth_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv')


# print the dataform top 10 and bottom 10
print(df.head(10))
print(df.tail(10))


# sort it based on sizeRank
df = df.sort_values('SizeRank')
print(df.head(10))
print(df.tail(10))



# store the dataform with negative growth on a particular date in a csv file
region_ids = df

neg_growth_2023_02_28 = region_ids[df['2023-02-28'] < 0]
neg_growth_2023_04_30 = region_ids[df['2023-04-30'] < 0]
neg_growth_2024_01_31 = region_ids[df['2024-01-31'] < 0]

print("RegionIDs with negative growth on 2023-02-28:")
print(neg_growth_2023_02_28['RegionID'].head(10))

print("RegionIDs with negative growth on 2023-04-30:")
print(neg_growth_2023_04_30['RegionID'].head(10))

print("RegionIDs with negative growth on 2024-01-31:")
print(neg_growth_2024_01_31['RegionID'].head(10))

neg_growth_2023_02_28[['RegionID', 'RegionName', 'RegionType']].to_csv(
    'processed_data/neg_growth_2023_02_28.csv', index=False)
neg_growth_2023_04_30[['RegionID', 'RegionName', 'RegionType']].to_csv(
    'processed_data/neg_growth_2023_04_30.csv', index=False)
neg_growth_2024_01_31[['RegionID', 'RegionName', 'RegionType']].to_csv(
    'processed_data/neg_growth_2024_01_31.csv', index=False)


# store the dataform with negative growth on a particular date in a csv file
region_ids = df

neg_growth_2023_02_28 = region_ids[df['2023-02-28'] > 0]
neg_growth_2023_04_30 = region_ids[df['2023-04-30'] > 0]
neg_growth_2024_01_31 = region_ids[df['2024-01-31'] > 0]


# print top 10 for each dates

print("RegionIDs with negative growth on 2023-02-28:")
print(neg_growth_2023_02_28['RegionID'].head(10))

print("RegionIDs with negative growth on 2023-04-30:")
print(neg_growth_2023_04_30['RegionID'].head(10))

print("RegionIDs with negative growth on 2024-01-31:")
print(neg_growth_2024_01_31['RegionID'].head(10))

neg_growth_2023_02_28[['RegionID', 'RegionName', 'RegionType']].to_csv(
    'processed_data/neg_growth_2023_02_28_p.csv', index=False)
neg_growth_2023_04_30[['RegionID', 'RegionName', 'RegionType']].to_csv(
    'processed_data/neg_growth_2023_04_30_p.csv', index=False)
neg_growth_2024_01_31[['RegionID', 'RegionName', 'RegionType']].to_csv(
    'processed_data/neg_growth_2024_01_31_p.csv', index=False)

