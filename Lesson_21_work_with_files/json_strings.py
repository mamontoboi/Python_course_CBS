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


dict_json = json.loads(string_data)
for item in dict_json['items']:
    print(type(item['var']))  # returns str as tuples in json are strings...


# to check in which coding was byte-like object before conversion into bytes
x = json.detect_encoding(b"\x80\x04\x95\xac\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x05items\x94]\x94(}\x94(\x8c\x05name1")
print(x)  # utf-8
