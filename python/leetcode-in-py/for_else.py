# coding=gbk

nums = [1, 2, 3, 4, 5]
is_odd_exist = False
for num in nums:
	if num % 2 == 1:
		is_odd_exist = True
		break

if is_odd_exist:
	print('Odd exist')
else:
	print('Odd not exist')
	
	
# for...else ��forѭ����������ʱ��������ͨ��break���������ģ�����ִ��else�е����

for num in nums:
	if num % 2 == 1:
		print('Odd exist')
		break
else:
	print('Odd not exist')
