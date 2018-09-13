#1
def input_nput_put_ut_t(input_str: str):
    org_list = []
    a = input_str
    while(len(a)>0):
        org_list.append(a)
        a = a[0:len(a)-1]
    return  org_list
print(input_nput_put_ut_t('hi! Mr.Adam, this is my homework'))

# add two vectors
def vector_addition(v1: list, v2: list) -> list:
	originallist = []
	for a in range(0,len(v1)):
		sum1 = v1[a] + v2[a]
		originallist.append(sum1)
	return originallist
print(vector_addition([1,2,3],[4,5,6]))

# two slice, same sum
def find_equal_sum_slice(list1: list, list2: list) -> [int, int, int, int]:
 for beginofa in range(len(list1)):
        for endofa in range(len(list1)):
            l1=list1[beginofa:endofa]
            for beginofb in range(len(list2)):
                for endofb in range(len(list2)):
                    l2=list2[beginofb:endofb]
                    while l1!=[] and l2!=[] and sum(l1)==sum(l2):
                        return beginofa, endofa - 1, beginofb, endofb - 1
print(find_equal_sum_slice([7,8,90],[6,9,91]))

# basic sort
def basic_sort(v1:list) -> list:
    org_list=[]
    a=v1
    for i in range(0,len(a)):
       org_list.append(min(a))
       a.remove(min(a))
    return org_list
print(basic_sort([3,6,2,4,5,12,9,7,1,8]))
