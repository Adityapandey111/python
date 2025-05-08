# english=int(input("Enter English mark "))
# math=int(input('Enter Maths mark '))
# science=int(input('Enter Science mark '))

# average=(english+math+science)/3
# print('Average marks ',average)

# a=list(range(5,12))
# print(a)

# age=-15
# print(age)

# if age>=18:
#     print('Can vote')
# elif age<18 and age>=0:
#     print('Can not vote')
# else:
#     print('Invalid age')

# for x in range(10):
#     print(x,end=" ")

# a=['Ram','Sita','Lakshman']

# for x in a:
#     print(x*3,end=" ")

# b=11

# while b>0:
#     print(b,end=" ")
#     b-=1

# string='Asdfghj5'

# print(string[-1:0:-1])

# for x in string:
#     print(x)

# print(string.islower())
# print(string.isupper())
# print(string.isalpha())
# print(string.isnumeric())
# print(string.upper())
# print(string.lower())

# for x in string:
#     if x<'a' or x>'z':
#         print('not lower')
#         break

# list=[x for x in range(51) if x and 1]
# print(list)

# arr=[1,2,3,4,5,6,7]

# sum=0

# while len(arr)>0:
#     if arr[0]%2==1:
#         sum+=arr[0]
    
#     print(arr[0])
#     arr.pop(0)  

# print(sum)

# str=" siyaram "
# print(str)
# print(str.strip().title())

# str='<<>>'

# words=str.strip().split()
# words.reverse()
# print(' '.join(words))
# print(st[3])
# tag_name="Jay"
# w=str[0:int(len(str)/2)] + tag_name + str[int(len(str)/2):len(str)]
# print(w)

# str="Ram Sita"

# dict={}
# for x in str:
#     if x in dict:
#         val=dict[x]
#         dict[x]=val+1
#     elif x!=' ':
#         dict[x]=1


# for key,value in dict.items():
#     print(key,value)

# tup=()
# tup.append(1)
# tup.append("ram")
# tup.append('sita')
# print(tup)

# def f(num):
#     x=1
#     y=2
#     return x,y,num

# ans=f(11)

# for c in ans:
#     print(c,end=" ")

# arr=[]

# for i in range(11):
#     arr.append(i)

# arr2=[11,51]
# arr2.extend(arr)
# arr2.sort()
# arr2.reverse()
# arr2.pop(0)
# print(arr2)


# class flashcard:
#     def __init__(self, word, meaning):
#         self.word = word
#         self.meaning = meaning
#     # def __str__(self):
      
#         #we will return a string 
#         # return self.word+' ( '+self.meaning+' )'
      
# flash = []
# print("welcome to flashcard application")

# #the following loop will be repeated until
# #user stops to add the flashcards
# while(True):
#     word = input("enter the name you want to add to flashcard : ")
#     meaning = input("enter the meaning of the word : ")
    
#     flash.append(flashcard(word, meaning))
#     option = int(input("enter 0 , if you want to add another flashcard : "))
    
#     if(option):
#         break
        
# # printing all the flashcards 
# print("\nYour flashcards")
# for i in flash:
#     print(">", i.word,i.meaning)


# class A:
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name
    
#     def accept(self,id,name):
#         obj=A(id,name)
#         ls.append(obj)

# ls=[]
# obj=A(1,'')
# obj.accept(11,"Ram")
# obj.accept(21,"Sita")

# for x in ls:
#     print(x.id,x.name)

# ls=[1,2,4,35,5]
# print(ls)
# ls.pop(1)
# print(ls)


# s = "!@#$%^&*12345678sdfghj"
# print(s.isdigit())    # True
# print(s.isalpha())    # False
# print(s.isalnum())    # True
# print(s.islower())    # True
# print(s.isspace())    # False

# str='He is the Avatar of the Lord Vishnu'
# f=open("file.txt",'w')
# fl=f.write(str)
# print(fl)

# def generate_table(n):
#     tab=""
#     for i in range(1,11):
#         tab+=f'{n} X {i} = {n*i}\n'
    
#     with open(f"tables/table_{n}",'w') as f:
#         f.write(tab)
    

# for i in range(2,21):
#     generate_table(i)

# words = ["the", "mat", "mouse","dog","barked","ran","hole","fence","found","home"]

# # content=""
# with open('file.txt') as f:
#     content=f.read()

# for word in words:
#     content=content.replace(word,'#'*len(word))

# with open('file.txt','w') as f:
#     f.write(content)

# dict1={'a':1,'b':2}
# dict2={'b':3,'c':5}
# m=dict2 | dict1

# print(m)

# import Union
# a:int=11
# b:int=21

# c:Union(string,int)='afsdf123'

# print(a+b)

nums = [1,3,1,2,2,121]
maxi=-1
for x in nums:
    maxi=max(maxi,x)

print(maxi)
# dct=dict()

# for x in nums:
#     if x in dct:
#         dct[x]=dct[x]+1
#     else:
#         dct[x]=1

# for key,value in dct.items():
#     print(key,value)