import utilities
import requests

print(utilities.add(3  ,  5))
import requests
try:
    response = requests.get("https://itwtech.com.ng/index.php")
    print(response.text)
except Exception  as e  :  
    print(f"This is my output for now {e}")    
