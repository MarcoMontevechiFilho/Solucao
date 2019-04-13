
def piramide(n):
    comp = 2*n-1;
    for k in range(0,n):
        for i in range(0,comp):
            if abs(i+1-n) > k:
                print('_',end='')
    
            elif abs(i+1-n) <= k:
                print('*',end='')
        print('\n')    

