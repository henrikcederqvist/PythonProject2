def foo(t):
    print("test")

foo("hej")

def fun1(x, y):
    return x * y

print(3, 5)

def fun1(x, y):
    return x * y

print(fun1(3, 5))

def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)

a = 5
def fun3(a):
    a += 1

a += 2
print(a)

def foo(i):
    return 2*i*i

def goo(x, y):
    return x(y)

a = goo(foo, 3);
print(a)

def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))


def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])

print(average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"]))