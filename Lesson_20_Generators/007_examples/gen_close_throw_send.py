def gen(num):
    for i in range(num):
        if i == 15:
            gen(i).close()  # ceases the generator at present step
        # elif i == 30:
        #     gen(i).throw(ValueError, ("Hell!"))
        elif i == 29:
            gen(i).send(None)  # Only None can be sent to a generator
        else:
            yield i


print(list(gen(31)))