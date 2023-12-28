# dictionary = A changeable, unordered collection of unique key: value pairs
# 				Fast because they use hashing, allow us to access a value quickly


capitals = {'USA':'Washington DC',
			'India': 'New Dehli',
			'China':'Beijing',
			'Russia':'Moscow',
			'Germany':'dot'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()



#print(capitals['Germany'])
#print(capitals.get('Germany'))
#rint(capitals.keys())
#rint(capitals.values())
#int(capitals.items())


for key,value in capitals.items():
	print(key, value)