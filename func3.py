def sum_of_list(numbers):
    return sum(numbers)
d = []

print('按q結束')
while True:
    name = input('請輸入數字: ')
    if name == 'q':
        break
    d.append(name)
d = list(map(int, d))
print('加起來總共是:', sum_of_list(d))