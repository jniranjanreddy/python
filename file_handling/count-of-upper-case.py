with open("test002") as fh:
    count = 0
    for line in fh:
        count += sum(1 for c in line if c.isupper())
    print(count) 