def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Paris")
# Output:
# name: Alice
# age: 25
# city: Paris


