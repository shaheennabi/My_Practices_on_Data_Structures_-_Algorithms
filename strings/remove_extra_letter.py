def findTheDifference(s, t):
    s_sorted = sorted(s)
    t_sorted = sorted(t)

    for i in range(len(s_sorted)):
        if s_sorted[i] != t_sorted[i]:
            return t_sorted[i]

    return t_sorted[-1]  # The extra char is at the end

result =  findTheDifference("publish", "pubblish")
print(result)