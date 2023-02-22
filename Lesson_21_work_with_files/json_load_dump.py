import json

data = {
        "items":
            [{"name": "name1",
              "price": "price1",
              "unit": "unit1",
              "qty": 'null',
              "var": "('var1', 'var2', 'var3')"},
             {"name": "name2",
              "price": "price2",
              "unit": 'null',
              "qty": "qty2",
              "var": "('var4', 'var5', 'var6')"}]
    }


# json.dump(data, file_name) sends the data into the file in json-like type. Indent to make the file pretty looked.
with open('json_test', 'w') as json_test_file:
    json.dump(data, json_test_file, indent=4)

# json.load(file_name) rcvs json data from file and converts in into readable format
with open('json_test', 'r') as json_test_file:
    loaded_data = json.load(json_test_file)

for item in loaded_data['items']:  # to loop through the values, corresponding to key 'items'
    print(item['name'], item['price'])  # name1 price1

for item in loaded_data['items']:
    del item['qty']  # to delete the 'qty' key from each item in dict
    print(item)

with open('json_test', 'w') as json_test_file:  # to dump the contents of the variable into the file
    json.dump(loaded_data, json_test_file, indent=2)

