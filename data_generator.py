import pandas as pd
from random import uniform
import random
names = pd.read_csv("baby-names.csv")

data = []
for name in names.name[100:300]:
    x, y = uniform((38.44 - 1), (48.44 + 1)), uniform((-100.295 - 1), (-100.295 + 1))
    phone_number = 0
    for i in range(10):
        phone_number += (10 ** i) * int(random.uniform(0, 10))
    data.append([name,phone_number,x,y])
df = pd.DataFrame(data)
df.to_csv("generated_data.csv")