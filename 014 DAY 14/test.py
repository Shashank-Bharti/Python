# def all_resources_available(g, r):
#     return all(g.get(key, 0) >= r[key] for key in r)

# Example dictionaries
g = {"water": 100, "milk": 60}
r = {"water": 20, "milk": 50}

# Check if all resources are available
if all(g.get(key, 0) >= r[key] for key in r):
    print(True)
else:
    print(False)