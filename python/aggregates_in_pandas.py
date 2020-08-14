import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

print(ad_clicks.groupby('utm_source').user_id.count().reset_index())

ad_clicks['is_click'] = ad_clicks.ad_click_timestamp.apply(lambda row: True if pd.isnull(row) else False)
print(ad_clicks.head())

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
)

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot.head())

print(ad_clicks.groupby('experimental_group').user_id.count()).reset_index()

clicks_ad_exp = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(clicks_ad_exp)

clicks_pivot_exp = clicks_ad_exp.pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
)

clicks_pivot_exp['percent_clicked'] = clicks_pivot_exp[True] / (clicks_pivot_exp[True] + clicks_pivot_exp[False])
print(clicks_pivot_exp)

a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A']
b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B']
print(a_clicks)

a_clicks_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

a_clicks_day_pivot = a_clicks_day.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
)

a_clicks_day_pivot['percent_clicked'] = a_clicks_day_pivot[True] / (a_clicks_day_pivot[True] + a_clicks_day_pivot[False])
print(a_clicks_day_pivot)

b_clicks_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()

b_clicks_day_pivot = b_clicks_day.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
)

b_clicks_day_pivot['percent_clicked'] = b_clicks_day_pivot[True] / (b_clicks_day_pivot[True] + b_clicks_day_pivot[False])
print(b_clicks_day_pivot)
