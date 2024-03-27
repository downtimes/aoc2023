# Playground for tesing some python stuff i'm unsure of

for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print(f"{animal} is a mammal")


# Closures in nested functions:
# We can use the nonlocal keyword to work with variables in nested scope which
# shouldn't be declared in the inner functions.
def create_avg():
    total = 0
    count = 0

    def avg(n):
        nonlocal total, count
        total += n
        count += 1
        return total / count

    return avg


avg = create_avg()
print(avg(3))  # => 3.0
print(avg(5))  # (3+5)/2 => 4.0
print(avg(7))  # (8+7)/3 => 5.0
