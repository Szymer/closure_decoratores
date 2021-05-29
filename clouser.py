def full_sentance(name):
    age = 36
    zd = "wow"

    def sentence(city):
        return f"I am {name}, age:{age} and com from {city}"

    return sentence

# s = full_sentance("Szymon")
# print(s("Krakow"))
# print(s.__closure__[1].cell_contents)
# print(s.__closure__[0].cell_contents)


def gen_uuid():
    idx = 0
    def nextt_id():
        nonlocal idx
        resoult = idx
        idx += 1
        return resoult

    return nextt_id

uuid = gen_uuid()

for _ in range(10):
    print("value of enclosing elemnets ", uuid.__closure__[0].cell_contents)
    print(uuid())
