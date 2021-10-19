import pickle
import datetime

data = [(datetime.date(2021, 10, 10), "Задача1"), (datetime.date(2021, 10, 11), "Задача2")]

with open("data.txt", "wb") as f:
    pickle.dump(data, f)

with open("data.txt", "rb") as f:
    data = pickle.load(f)
print(data)