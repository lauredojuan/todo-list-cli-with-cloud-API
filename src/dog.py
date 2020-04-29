import requests
import json

# also 
# import requests, json

# r = requests.get('https://dog.ceo/api/breed/hound/images')
# response = r.json()
# myList = response["message"]
# # print(response["message"])
# for x in myList:
#     print(x)
r = requests.put('https://assets.breatheco.de/apis/fake/todos/user/lauredojuan', data= {"key":json.dumps([{"label": "Make the bed", "done": False}])})
print(r.json())