

# def flatten(items):
#     for i, x in enumerate(items):
#         while i < len(items) and isinstance(items[i], list):
#             print(items[i])
#             items[i:i+1] = items[i]
# #            print(items[i])
#     return items

def flatten2(iterable):
    iterator, sentinel, stack = iter(iterable), object(), []
    while True:
        value = next(iterator, sentinel)
        if value is sentinel:
            if not stack:
                break
            iterator = stack.pop()
        elif isinstance(value, str):
            yield value
        else:
            try:
                new_iterator = iter(value)
            except TypeError:
                yield value
            else:
                stack.append(iterator)
                iterator = new_iterator

essai_1 = [1, 2, [3, [4, 5], [6]], 7]
essai_2 = [1, 2, [3, 4], 5]


#print(flatten(essai_1))

def main():
    data = [1, 2, [3, 4, [5], []], [6]]
    print(list(flatten2(essai_1)))

main()
