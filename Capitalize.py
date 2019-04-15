from timeit import timeit
def solve(s):
    return " ".join([str(x).capitalize() for x in str(s).split(" ")])


if __name__ == "__main__":
    print(solve("hello   world  lol"))
    #print(timeit("solve('hello   world  lol')", "from __main__ import solve"))
