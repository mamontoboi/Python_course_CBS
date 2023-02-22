import shelve

data = {
        "items":
            [{"name": "name1",
              "price": 6500,
              "unit": "unit1",
              "qty": 'null',
              "var": "('var1', 'var2', 'var3')"},
             {"name": "name2",
              "price": 5000,
              "unit": 'null',
              "qty": "qty2",
              "var": "('var4', 'var5', 'var6')"}]
    }

with shelve.open('shelve_file', 'c', writeback=True) as file:  # opens the file as shelve object
    """
    'r' -- Open existing database for reading only (default)
    'w' -- Open existing database for reading and writing
    'c' -- Open database for reading and writing, creating it if it doesn’t exist
    'n' -- Always create a new, empty database, open for reading and writing
    writeback=True is necessary to be able to apply changes via .sync() during the use of file.
    """
    for key, value in data.items():
        file[key] = value  # fills the files with key-value pairs

    print(file['items'][1])  # prints the 1st elements of list, that serves as value for key 'items'

    print(file['items'][0]['qty'])  # returns value of the corresponding key

    flag = 'items' in file  # checks whether the key is inside the shelf file
    print(flag)

    del file['items'][1]  # to delete the 1st element in the list corresponding to key 'items'
    file.sync()  # it was necessary to save the changes in file.
    print(file['items'])  # because of sync() now only 0 element of the list is displayed



