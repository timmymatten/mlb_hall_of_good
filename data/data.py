import pandas as pd

data = pd.read_csv('mlb_season_data.csv')

data1990present = data[data['season'] >= 1990]

data1990present['full_name'] = data1990present['first_name'] + ' ' + data1990present['last_name']
data1990present = data1990present.drop(['first_name', 'last_name'], axis=1)
cols = ['full_name'] + [col for col in data1990present.columns if col != 'full_name']
data1990present = data1990present[cols]

# Aggregate player stats into career totals
player_agg = data1990present.groupby('full_name').agg({
    'hits': 'sum',
    'homeruns': 'sum',
    'rbi': 'sum',
    'runs': 'sum',
    'stolen_bases': 'sum',
    'walks': 'sum',
    'strikeouts': 'sum',
    'games_played': 'sum',
    'at_bats': 'sum',
    # For averages/percentages, take mean (career rate stat would usually be weighted)
    'batting_average': 'mean',
    'on_base_plus_slugging': 'mean'
}).reset_index()

# Save both versions if you want
data1990present.to_csv('data_1990_present.csv', index=False)      # season-level
player_agg.to_csv('player_career_stats.csv', index=False)         # career totals
