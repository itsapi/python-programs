n = 4
total = 25

bins = [[] for bin in range(n)]

fit = True
while fit:
    inp = int(input())
    fit = False
    for bin in bins:
        if sum(bin) + inp <= total:
            bin.append(inp)
            fit = True
            break
    print(bins)
    print(', '.join(str(sum(bin)) for bin in bins))

