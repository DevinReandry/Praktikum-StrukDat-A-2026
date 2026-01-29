print(18>9)
print(10 == 10)
print(88<10)

a = 333
b = 900
if b > a:
    print("b lebih bear dari a")
else:
    print("b lebih kecil dari a")

print(bool("L yagami"))
print(bool(67))

x = 39
y = "kucing"
print(bool(x))
print(bool(y))

bool("abcdefgh")
bool(789)
bool(["aku", "mau", "tidur"])


bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

def ToF():
    return True

print(ToF())


def TOF():
    return True

if TOF():
    print("Yep")
else:
    print("Nope")


x = 1000
print(isinstance(x, int))