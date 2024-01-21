import random

x = random.randint(1 ,100)
y = random.randint(1 ,100)

for i in range(10):
    x = random.randint(1 ,y*x)
    y = random.randint(1 ,x*y)
    echo base_convert(x, 10, 64)
