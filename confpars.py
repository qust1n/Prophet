import base64
from rich.console import Console 
console = Console()

try:
	data = input("Enter api_id: ")
	
	encodedBytes = base64.b64encode(data.encode("utf-8"))
	encodedStr = str(encodedBytes, "ascii")
	
	data2 = input("Enter api_hash: ")
	
	encodedBytes2 = base64.b64encode(data2.encode("utf-8"))
	encodedStr2 = str(encodedBytes2, "utf-8")
	
	with open('config.py', 'w') as file:
		file.write("api_id = " + "'" + encodedStr + "'\n"
		"api_hash = " + "'" + str(encodedBytes2, "utf-8") + "'")
	
except Exception:
	console.print_exception(show_locals=True)
