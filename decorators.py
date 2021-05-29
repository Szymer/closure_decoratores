def capitalize(fn):
    def inner(name):
          resoult = fn(name)
          resoult = resoult.replace(name, f'MR.{name}')
          return resoult
    return inner



@capitalize
def hello(name):
    return f"Hello {name}"

@capitalize
def goodbye(name):
    return f"Bye {name}"
print(hello("szymon"))
print(goodbye("szymon"))


