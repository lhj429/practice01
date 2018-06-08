s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

dict = {}
split = s.upper().replace(',', "").replace('.', "").replace('\n', "").split(" ")
split.sort()

for s in split:
    if s in dict.keys():
        dict[s] += 1
    else:
        dict[s] = 1

for key in dict.keys():
    print(key)

for key, value in dict.items():
    print("{}:{}".format(key, value))