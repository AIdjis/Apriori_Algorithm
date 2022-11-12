import pandas as pd
data=pd.read_csv('data.csv',)

data=data.values
while True:
    try:
        minsup=int(input('please Enter Minimum Support: '))
        break
    except Exception :
        print('please enter a intger number!!')

class Apirori:

    # cleaning the data by removing the None values
    def preprossing(data):
        newdata=[]
        for i in range(len(data)):
            transaction=[]
            for j in range(len(data[i])):
                if str(data[i,j])=='nan':
                    continue
                else:
                    transaction.append(data[i,j])
            newdata.append(set(transaction))
        return newdata
    
    def firstitemset(data):
        firstitemset=[]
        for i in data:
            for j in i:
                item=set({})
                item.add(j)
                if item in firstitemset:
                    continue
                else:
                    firstitemset.append(item)
        return firstitemset

    def frequent_candidate(data,candidate,minsup):
        frequent_item={}
        for i in candidate:
            support=0
            for j in data:
                element=[ s for s in i if s in j ]
                if len(element)==len(i):
                    support+=1
            if support >=minsup:
                frequent_item[tuple(i)]=support
        return frequent_item
    
    def frequent_pattern(frequent_itemset):
        pattern_generate=[]
        for i in frequent_itemset:
           pattern_generate.append(set(i))
        return pattern_generate

    def candidate_itemset(data,frequent_itemset,scan):
        if scan==1:
            return Apirori.firstitemset(data)
        else:
            candidate=[]
            i=0
            while i<len(frequent_itemset):
                j=i+1
                while j<len(frequent_itemset):
                    pattren=list(dict.fromkeys(list(frequent_itemset[i])+list(frequent_itemset[j])))
                    if set(pattren) not in candidate and len(pattren)==scan:
                        candidate.append(set(pattren))
                    j+=1
                i+=1
        return candidate
    
    def frequent_itemset(data):
        result=[]
        frequent_itemset=[]
        scan=1
        while True:
            candidate_itemset=Apirori.candidate_itemset(data,frequent_itemset,scan)
            frequent_itemset=Apirori.frequent_candidate(data,candidate_itemset,minsup)
            if len(frequent_itemset)==0:
                break
            result.append(frequent_itemset)
            frequent_itemset=Apirori.frequent_pattern(frequent_itemset)
            scan+=1
        return result

    def show(result):
        print('/////////// frequent items set for each level /////////////')
        level=1
        for i in result:
            print(str(level) + ':',end=' ')
            for j in i:
                
                print('  '+str(set(j)) +':'+str(i[j]),end=' ')
            print('\n')
            level+=1

data=Apirori.preprossing(data)
result=Apirori.frequent_itemset(data)  
Apirori.show(result)









