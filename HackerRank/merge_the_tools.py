def merge_the_tools(string, k):
    temp = []
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item) # Se adauga in array-ul temp caracterul
        if len_temp == k:
            print(''.join(temp)) # Se afiseaza array-ul
            temp = []
            len_temp = 0
            
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)