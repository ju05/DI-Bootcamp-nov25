# API

import requests
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

response = requests.get('https://musicapi.x007.workers.dev/search?q=Pathaan&searchEngine=gaama')

print(response)

data = response.json()
print(data.get('title'))

with open(dir_path + '\jokes.json', 'w')  as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    print('file was created')