import nltk
from pdfreader import *

def dist_between(a, b, pos):
    mini = 10000
    lum = 0 
    mul = 0
    for i in range(len(a)):
        """lim = [[b[k] - a[i],a[i],b[k]] for k in range(len(b)) if(b[k] > a[i])]
        mini = min(lim)
        """
        for k in range(len(b)):
            if(a[i] < b[k] and b[k]-a[i] < mini):
                mini =  b[k] - a[i]
                lum = a[i]
                mul = b[k]
    return [mini, lum, mul, pos]
        
list_of_dic = ret_dic()
#print(list_of_dic)
def sortSecond(val): 
    return val[1]  
query = input("Enter query")
q_terms = query.split(" ")
#arr_of_ranks = []
rank = []
for doc_term in range(len(list_of_dic)):
    for i in range(len(q_terms) - 1):    
        a = q_terms[i]
        b = q_terms[i+1]
        if(not a in list_of_dic[doc_term].keys() or not b in list_of_dic[doc_term].keys()): 
            continue
        dic_a = list_of_dic[doc_term][a]
        dic_b = list_of_dic[doc_term][b]
        rank.append(dist_between(dic_a, dic_b, doc_term+1))

rank.sort()
print('\n' )
print(rank)
