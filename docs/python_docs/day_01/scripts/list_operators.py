fruits: list[str] = ["apple", "banana", "cherry"]

print("Element at 1: ", fruits[1])
print("Last element: ", fruits[-1])

fruits.append("mango")
fruits.insert(1, "watermelon")

last_fruit: str = fruits.pop()
fruits.remove("apple")
