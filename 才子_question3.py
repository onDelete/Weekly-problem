def bubble(s):
    for i in range(len(s)):
        for (j) in range(i, len(s)):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]
    return s
