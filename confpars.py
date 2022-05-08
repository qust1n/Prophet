try:
	api_id = int(input("Enter api_id: "))
	api_hash = input("Enter api_hash: ")
	
	with open('config.py', 'w') as file:
		file.write("api_id = " + str(api_id)+
						 "\napi_hash = " + "'" +str(api_hash) + "'")
		
		
	print("\n\033[32mDone!")
		
except ValueError:
	print("\n\033[31mapi_id consists of numbers only")