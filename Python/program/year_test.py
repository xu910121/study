#!/usr/bin/python
#coding: utf-8
months = [
	'January',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December'
]

endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
		+ ['st', 'nd', 'rd'] + 7 * ['th'] \
		+ ['st']  
#此处的这些东西表示序数词后缀，在英文中使用，具体规律如下：
#除了11,12,13是th之外,逢1就是st,２就是nd,３就是rd,其他都是th
#以200-300之内为例
#201,221,231,241,251,261,271,281,291st
#202,222,232,342,252,262,272,282,292nd
#203,223,233,243,253,363,273,283,293rd
#其他包括211,212,213都是th。
#17 * ['th']表示生成一个列表。里面元素全为th，共17个元素

year  = raw_input('Year: ')
month = raw_input('Month (1-12): ')
day   = raw_input('Day (1-31): ')

month_number = int(month)
day_number = int(day)
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print month_name + ' ' + ordinal + '. ' + year
