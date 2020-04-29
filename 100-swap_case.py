def swap_case(s):
    i=len(s)
    p=[0 for k in range(i)]
    for j in range(i):
        if s[j].islower():
            p[j]=s[j].upper()
        else:
            p[j]=s[j].lower()
    h=''.join(p)

        
        
    return h

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)