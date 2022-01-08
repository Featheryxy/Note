def build_person(first_name, last_name, age=''):
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person
	
me = build_person('Milo', 'Ye', 23)
print(me)

def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
	
user_profile = build_profile('albert', 'einstein', \
							location = 'princeton', \
							field = 'physics')
print(user_profile)
