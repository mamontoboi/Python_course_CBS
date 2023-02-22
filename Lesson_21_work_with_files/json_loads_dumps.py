import json

string_data = """{
    "items": [
        {
            "name": "name1",
            "price": "price1",
            "unit": null,
            "qty": false,
            "var": "('var1', 'var2', 'var3')"
        },
        {
            "name": "name2",
            "price": "price2",
            "unit": null,
            "qty": true,
            "var": "('var4', 'var5', 'var6')"
        }
    ]
}"""


# json.loads(string data) returns the dictionary data from the json-like string object
dict_json = json.loads(string_data)
print(dict_json)  # print the dictionary, made of initial string

print(type(dict_json['items']))  # list

for item in dict_json['items']:  # loop through the list of items
    print(item)

for item in dict_json['items']:  # loop through the list of items
    print(item['qty'])  # each 'qty' => each item in list => key 'items' => dict_json

for item in dict_json['items']:
    del item['unit']  # deletes the 'unit' key => each item in list => key 'items' => dict_json


# json.dumps(data) returns the data converted in json object. Indentation to make it pretty looked.
new_string = json.dumps(dict_json, indent=2, sort_keys=True)  # dumps the modified initial string into a new string. sort_keys to sort in alphabetical order
print(new_string)

for item in dict_json['items']:
    print(type(item['var']))