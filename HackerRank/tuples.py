if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split()) # Se creeaza un array
    t = () # Tuple
    for x in integer_list:
        t += (x,) # Generare tuple
    
    print(hash(t)) 
