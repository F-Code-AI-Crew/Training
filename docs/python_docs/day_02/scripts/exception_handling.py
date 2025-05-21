def process_and_divide(data, index, divisor):
    try:
        raw = data[index]
        print(f"Get raw = {raw}")

        number = int(raw)
        print(f"Cast to integer: {number}")
        result = number / divisor
        return f"Result: {result}"
    except IndexError:
        return "Error: Index out of range!"

    except ValueError:
        return f"Error: '{raw}' cannot be parsed into number!"

    except ZeroDivisionError:
        return "Error: Cannot divide by 0!"

    finally:
        print("Always run!") # run before exception handling


data = ["10", "abc", "30"]

print(process_and_divide(data, 0, 2)) # valid case
print("==========================")

print(process_and_divide(data, 5, 2)) #index of of range
print("==========================")

print(process_and_divide(data, 1, 2)) # parse error
print("==========================")

print(process_and_divide(data, 2, 0)) # zero division error
print("==========================")