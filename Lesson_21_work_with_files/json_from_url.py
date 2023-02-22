import json


from urllib.request import urlopen

with urlopen('https://api.github.com') as response:
    source = response.read()

data = json.loads(source)
print(type(data))  # returns dict

for key in data:
    print(key)  # returns all keys in the json dict

print(data['starred_url'])  # returns the value of corresponding key

print(len(data['starred_url']))  # returns length of the value of corresponding key

for item in data:
    if item.find('rep') > 0:  # returns all keys that contain 'org' in their names
        print(item)

del data['public_gists_url']  # to delete the entry from the dict

for item in data:
    print(item)

# to dump the data into the file
with open('url_json.txt', 'w') as url_file:
    json.dump(data, url_file, indent=2, sort_keys=True)

# to add new line to the dict and to dump it into the file
with open('url_json.txt', 'w') as url_file:
    data['new_user'] = "Bogdan"
    json.dump(data, url_file, indent=2)

# to get the value of key in json file
with open('url_json.txt', 'r') as url_file:
    line = json.load(url_file)
    print(line['new_user'])

