def numbers_in_lists(string):
    i=0
    L=[]
    while i<len(string):
        L.append(int(string[i]))
        i=i+1
    
    j=0
    K=[]
    M=[]
    for h in L:
        if h>j:
            j=h           
            if M!=[]:
                K.append(M)
            K.append(h)
            M=[]
        else:
            M.append(h)                           
    K.append(M)
    if [] in K:
        K.remove([])
    return K        
            
string = '543987'
print numbers_in_lists(string) 

string= '987654321'
print numbers_in_lists(string) 

string = '455532123266'
print numbers_in_lists(string)

string = '123456789'
print numbers_in_lists(string)
