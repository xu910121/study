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
#�˴�����Щ������ʾ�����ʺ�׺����Ӣ����ʹ�ã�����������£�
#����11,12,13��th֮��,��1����st,������nd,������rd,��������th
#��200-300֮��Ϊ��
#201,221,231,241,251,261,271,281,291st
#202,222,232,342,252,262,272,282,292nd
#203,223,233,243,253,363,273,283,293rd
#��������211,212,213����th��
#17 * ['th']��ʾ����һ���б�����Ԫ��ȫΪth����17��Ԫ��

year  = raw_input('Year: ')
month = raw_input('Month (1-12): ')
day   = raw_input('Day (1-31): ')

month_number = int(month)
day_number = int(day)
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print month_name + ' ' + ordinal + '. ' + year
