def html_tag(tag="H1"):
    def wrapper(fn):
        def inner(name):
            resoult = f"<p>{fn(name)}<\p>"
            resoult = resoult.replace(name, f"<{tag}>{name}</{tag}>")
            return resoult
        return inner
    return wrapper


def capitalize(fn):
    def inner(name):
          # resoult = f"<p>{fn(name)}<\p>"
          # resoult = resoult.replace(name, f"<h1>{name}</h2>")
          return fn(name.title())
    return inner


@capitalize
@html_tag("h2")
def hello(name):
    return f"Hello {name}"


@capitalize
@html_tag("span")
def goodbye(name):
    return f"Bye {name}"


print(hello("szymon"))
print(goodbye("szymon"))


