def task(array):
    if array.find('0') != -1:
        result = array.find('0')
    else:
        result = "Символ '0' отсутствует"
    return result


print(task("111111111111111111111111100000000"))
