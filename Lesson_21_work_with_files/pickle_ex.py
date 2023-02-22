import pickle

data = {
        "items":
            [{"name1": "name1",
              "price1": "price1",
              "unit1": "unit1",
              "qty1": "qty1",
              "var1": "('var1', 'var2', 'var3')"},
             {"name2": "name2",
              "price2": "price2",
              "unit2": "unit2",
              "qty2": "qty2",
              "var2": "('var4', 'var5', 'var6')"}]
    }

# pickle.dump(data, file_name) sends the data into the file in bytes
with open('pickle_test', 'wb') as pickle_out:
    pickle.dump(data, pickle_out)

# pickle.load(file_name) rcvs data in bytes from file and converts in into readable format
with open('pickle_test', 'rb') as pickle_in:
    rcv_data = pickle.load(pickle_in)
    print(rcv_data)

# pickle.dumps(data) returns the data, converted into bytes. Without sending in to file
x = pickle.dumps(rcv_data)
print(x)

# pickle.loads(byte-like data) returns the original readable data from the byte-like object
y = pickle.loads(x)
print(y)
