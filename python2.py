mystr = 'matthias biswas'

'''for elements in mystr:
    print(elements )
for elements in 'hello':
    print(elements)
'''
'''tup = (45,4546.1221,4523,4856.23)
#tupe = str(tup)
#print(type(tupe))
for item in tup:
    print (item,sep='')

mylist = [(908,45),(456,12),(84,89),(4895,1)]
#print(len(mylist))
#print(mylist)

############   TUPLE UNPACKING  ############ 

for i in mylist:
    print(i)
                    ######## SAME but there are some limitations
for (a,b) in mylist:
    print(a,b)

for (a,b) in mylist:
    print('({}, {})'.format(a,b))




############   TUPLE UNPACKING  ############ 

for i in mylist:
    print(i)
                    ######## this is why the .format method is important
                    ######## you can not do tuple unpacking with conditions
                    ######## without .format() method  
for (a,b) in mylist:
    if a % 2 == 0  and  b % 2 == 0:  
        print('({}, {})'.format(a,b))'''


############    DICTIONARY    ###############

d = {'k1': 23,'k2': 78,'k3': 3,'k4': 54}

'''for i in d:
    print(i)

for i in d.values():
    print(i)
'''
'''
e = 0
for a,b in d.items():
    e += b                  ########## DICTIONARIES WITH CONDITIONS
    #print(e)
    #print('({}, {})'.format(a,b))
    if e % 2 == 0:
        print(f'{e} is even')
    else:
        print(f'{e} is odd')'''


d = {'k1':21, 'k2': 54, 'k3':75, 'k4':64, 'k5':17, 'k6':26}
numlist = []
#n = int(input('number of elements in numlist: '))

even = []
odd = []
even_d = []
odd_d = []
uilist = 0
'''def u_input(uinputlist):
    for _ in range(0,n):
        ele = int(input('enter elements of list: '))
        numlist.append(ele)

def check(lists):
    for i in numlist:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)'''

def check_dic(dictionariess):
    for k,v in d.items():
        if v % 2 == 0:
            even_d.append(v)
        else:
            odd_d.append(v)

#u_input(uilist)
#check(numlist)
check_dic(d)
#print(f'Numlist: {numlist}')



sorted_even_d = sorted(even_d)
sorted_odd_d = sorted(odd_d)

print(f'Even_D: {sorted_even_d}')
print(f'Odd_D: {sorted_odd_d}')























