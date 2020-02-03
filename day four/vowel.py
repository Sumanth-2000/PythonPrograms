dict = {0:'bourbon',1:'eclairs',2:'marshmallow',3:'kitkat',4:'oreo',5:'jelly'}
print(dict)
list = list(dict.values())
print(list)
for each in range(len(list)):
    if list[each][0] in "aeiou":
        if each+1<len(list)-1:
            temp=list[each];
            list[each]=list[each+1]
            list[each+1]=temp
        else:
            print("Can't replace")
print(list)
a= {i: list[i] for i in range(0, len(list))}
print(a)