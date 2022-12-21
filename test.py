a = [{"petko":100, "age":20}, {"petkos":200, "age":22}]
index = 0
index = [(i, sublist[x]) for i, sublist in enumerate(a) for x in sublist if x == "petkos"]

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)

print(power(2, 2))