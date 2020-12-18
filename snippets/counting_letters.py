from collections import Counter

if __name__ == '__main__':
    sentence = "This is a common interview question"
    counted = Counter(sentence)
    counted.pop(' ') #optionally getting rid of the space
    print(*counted.most_common(1))

    #manually:
    counted_with_dict = dict()
    for c in sentence:
        counted_with_dict[c] = counted_with_dict.get(c, 0) + 1
    counted_with_dict.pop(' ')
    print(sorted(counted_with_dict.items(), key=lambda x: -x[1])[0])
