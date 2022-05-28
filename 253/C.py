Q=int(input())
def query_1(query_list,ans_list):
    print("==========")
    print("query_1")
    print(query_list)
    print(ans_list)
    ans_list.append(query_list[1])
    print(ans_list)
    print("==========")
    return ans_list
    
def query_2(query_list,ans_list):
    print("==========")
    print("query_2")
    print(query_list)
    print(ans_list)
    #################
    c=query_list[2]
    s_in_x=ans_list.count(query_list[1])
    
    if(c<=s_in_x):
        for k in range(c):
           ans_list.remove(query_list[1])
    else:
        for k in range(s_in_x):
            ans_list.remove(query_list[1])
    print("==========")
    return ans_list

def query_3(query_list,ans_list):
    if(len(ans_list)!=0):
        print("==========")
        print("query_3")
        print(query_list)
        print(ans_list)
        print("==========")
        print(max(ans_list)-min(ans_list))
        return ans_list
    else:
        return ans_list

ans_list=[]
for i in range(Q):
    query_list=list(map(int,input().split()))
    if(query_list[0]==1):
        ans_list=query_1(query_list,ans_list)
    elif(query_list[0]==2):
        ans_list=query_2(query_list,ans_list)
    elif(query_list[0]==3):
        ans_list=query_3(query_list,ans_list)
