import pandas as pd
import numpy as np

# 1.时间特征拆解
# 构造时间数据
date_time_str_list = [
    '2019-01-01 01:22:26', '2019-02-02 04:34:52', '2019-03-03 06:16:40',
    '2019-04-04 08:11:38', '2019-05-05 10:52:39', '2019-06-06 12:06:25',
    '2019-07-07 14:05:25', '2019-08-08 16:51:33', '2019-09-09 18:28:28',
    '2019-10-10 20:55:12', '2019-11-11 22:55:12', '2019-12-12 00:55:12',
]

df = pd.DataFrame({'date_time': date_time_str_list})
print(df)
# 把字符串格式的时间转换成Timestamp格式
df['date_time'] = df['date_time'].apply(lambda x: pd.Timestamp(x))
print(df)
# get year
df['year'] = df['date_time'].apply(lambda x: x.year)
print(f'year: {df["year"]}')

# get month
df['month'] = df['date_time'].apply(lambda x: x.month)
print(f'month: {df["month"]}')

# get day
df['day'] = df['date_time'].apply(lambda x: x.day)
print(f'day: {df["day"]}')

# get hour
df['hour'] = df['date_time'].apply(lambda x: x.hour)
print(f'hour: {df["hour"]}')

# minute
df['minute'] = df['date_time'].apply(lambda x: x.minute)
print(f'minute: {df["minute"]}')

# second
df['second'] = df['date_time'].apply(lambda x: x.second)
print(f'second: {df["second"]}')

# 一年中的第几天
df['day_of_year'] = df['date_time'].apply(lambda x: x.dayofyear)
print(f'day_of_year: {df["day_of_year"]}')

# 一年中的第几周
df['week_of_year'] = df['date_time'].apply(lambda x: x.week)
print(f'week_of_year: {df["week_of_year"]}')

# 一天中哪个时间段：凌晨、早晨、上午、中午、下午、傍晚、晚上、深夜；
period_dic = {
    23: '深夜', 0: '深夜', 1: '深夜',
    2: '凌晨', 3: '凌晨', 4: '凌晨',
    5: '早晨', 6: '早晨', 7: '早晨',
    8: '上午', 9: '上午', 10: '上午', 11: '上午',
    12: '中午', 13: '中午',
    14: '下午', 15: '下午', 16: '下午', 17: '下午',
    18: '傍晚',
    19: '晚上', 20: '晚上', 21: '晚上', 22: '晚上',
}
df['period_of_day'] = df['hour'].map(period_dic)
# 一年中的哪个季度
season_dict = {
    1: '春季', 2: '春季', 3: '春季',
    4: '夏季', 5: '夏季', 6: '夏季',
    7: '秋季', 8: '秋季', 9: '秋季',
    10: '冬季', 11: '冬季', 12: '冬季',
}
df['season'] = df['month'].map(season_dict)
print(df)

# 2）时间特征判断
# 是否闰年
df['是否闰年'] = df['date_time'].apply(lambda x: x.is_leap_year)
df['是否月初'] = df['date_time'].apply(lambda x: x.is_month_start)
df['是否月末'] = df['date_time'].apply(lambda x: x.is_month_end)
df['是否季节初'] = df['date_time'].apply(lambda x: x.is_quarter_start)
df['是否季节末'] = df['date_time'].apply(lambda x: x.is_quarter_end)
df['是否年初'] = df['date_time'].apply(lambda x: x.is_year_start)
df['是否年尾'] = df['date_time'].apply(lambda x: x.is_year_end)
df['是否周末'] = df['date_time'].apply(lambda x: True if x.dayofweek in [5, 6] else False)

# 是否公共假期
public_vacation_list = [
    '20190101', '20190102', '20190204', '20190205', '20190206',
    '20190207', '20190208', '20190209', '20190210', '20190405',
    '20190406', '20190407', '20190501', '20190502', '20190503',
    '20190504', '20190607', '20190608', '20190609', '20190913',
    '20190914', '20190915', '20191001', '20191002', '20191003',
    '20191004', '20191005', '20191006', '20191007',
]  # 此处未罗列所有公共假期
df['日期'] = df['date_time'].apply(lambda x: x.strftime('%Y%m%d'))
df['是否公共假期'] = df['日期'].apply(lambda x: True if x in public_vacation_list else False)
# 是否营业时间
df['是否营业时间'] = False
df['小时'] = df['date_time'].apply(lambda x: x.hour)
df.loc[((df['小时'] >= 8) & (df['小时'] < 22)), '是否营业时间'] = True

df.drop(['日期', '小时'], axis=1, inplace=True)
print(df)
