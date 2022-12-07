#!/usr/bin/env python
# coding: utf-8

# <div class="alert alert-info"  >
#     <h1><center>تمرین اول دوره پایتون در علم داده</center></h1>
# </div>

#  <div style="direction:rtl">
#  <h2 align="right"> برای هر پرسش کدهایی بنویسید که پاسخ خواسته شده را تولید کند</h2>
#  </div>

# <h4 align="right"> هشت به توان نه را محاسبه نمایید </h4>

# In[1]:


#answer=134217728
8**9


# <p>پاسخ عبارات زیر را بدس آورید </p>
#     <p> 25 * (10 + 6) </p>
#     <p> 25 * 10 + 6 </p>
#     <p>25 + 10 * 6  </p>
#     

# In[4]:


# answer=400
25*(10+6)


# In[5]:


25 * 10 + 6


# In[6]:


25 + 10 * 6


# <h4 align="right"> نوع (تایپ) داده ی نتیجه عبارت 7 * 2.6 + 31 چیست؟ </h4>
# 
# 

# In[7]:


#answer= float
type( 7 * 2.6 + 31 )


# <h4 align="right"> عدد 26.26632 را تا دو رقم اعشار گرد کنید </h4>
# 

# In[8]:


round(26.26632,2)


# <div style="direction:rtl">
#     <h4 align="right"> ابتدا رشته زیر را تعریف نمایید و سپس با استفاده از متد های رشته، آن را به کلمات تشکیل دهنده تفکیک نموده و در یک لیست ذخیره کنید. </h4>
# 
# <div style="direction:ltr">
# s = "Hi this is a robot! Good morning!"

# In[10]:


# ans= ['Hi', 'this', 'is', 'a', 'robot!', 'Good', 'morning!']

s='Hi this is a robot! Good morning!'
ans=s.split()
print(ans)


# <div style="direction:rtl">
#     <p> ابتدا دو متغیر زیر را تعریف نمایید : </p>
#     <p> product = "laptop"  </p>
#     <p> price = 350 </p>
#     <p>حال با دو روش مختلف  جمله ی زیر را نمایش دهید :  </p>
#     <p>The price of laptop is 350 dollars.  </p>
#     <p> اول: به صورت عادی </p>
#     <p>دوم : با استفاده از متد قالب بندی رشته </p>
#     (format)
#  </div> 
# 
# 

# In[27]:


product='laptop'
price=350

print('the price of this',product,'is',price,'dollars')
print('the price of this %s is %d dollars' %(product,price ))


# In[13]:


# [جواب در باکس 27]


# In[14]:


# [جواب در باکس 27]


# <h4 align="right"> ابتدا رشته زیر را تعریف نمایید . </h4>
# m = 'I am a data scientist!'
# 

# In[29]:


m = 'I am a data scientist!'


# <h4 align="right"> حال کاراکترهای زیر را از رشته بیابید </h4>
# 'i'   ,  
# 'c'

# In[30]:


for i in m:
    if i=='i'or i=='c':
        print(i)


# In[33]:


for i in m:
    if  i=='c':
        print(str(i))


# In[34]:


txt = "Hello World"[::-1]
print(txt)


# <h4 align="right">رشته را معکوس کنید   </h4>

# In[36]:


#ans='!tsitneics atad a ma I'
print(m[::-1])


# <h4 align="right">در رشته زیر بررسی کنید که آیا هر حرف از نوع حروف بزرگ است؟  </h4>

# In[38]:


# False
s='w'
s.istitle()


# <div style="direction:rtl">
#     <h4 align="right"> "w" </h4>
#     <h4 align="right">در رشته زیر چندبار  ظاهر می شود؟  </h4>
#     <h4 align="right"> می توانید با جستجو و تحقیق متد مناسب را بیابید؟</h4>
#     
#  </div>

# In[40]:


# 12
t=0
m = 'I am a data scientist!'
for i in m:
    if i=='a':
        t+=1
print(t)
    


# <h4 align="right">آدرس سایت را از ایمیل زیر  جدا کنید؟ </h4>

# In[43]:


# ans='yahoo.com'
s = 'John_Smith@yahoo.com'
for i in range(0,len(s)):
    if s[i]=='@':
        print(s[i+1:])


# <div style="direction:rtl">
#     <h4 align="right"> در لیست زیر به جای کلمه </h4>
#     <h4 align="right"> window  </h4>
#     <h4 align="right"> کلمه  </h4>
#     <h4 align="right"> ِdoor  </h4>
#         <h4 align="right"> ِرا بگذارید </h4>
#  </div>

# In[51]:


lst1 = [4,56,['a',4,'window'],['4.5', ['abc']]]


# In[56]:


# ans= [4, 56, ['a', 4, 'door'], ['4.5', ['abc']]]
lst1[2][2]='door'
lst1


# <h4 align="right">به کمک ایندکسینگ در لیست های تو در تو، کلمه زیر را خروجی دهید  </h4>
# 'Tehran'

# In[58]:


lst2 = [1,2,[3,4],['a',['abc',200,['Tehran', 3]],23,'c'],1.5,7]


# In[64]:


# ans='Tehran'
lst2[3][1][2][0]


# <h4 align="right">به کمک ایندکسینگ در ساختار تودرتوی زیر ، کلمه زیر را خروجی دهید  </h4>
# 'Tehran'

# In[65]:


d = {'ab':[45,56,5.4,{'Countries':['Spain','USA','Germany',{'Iran':[24,'Tehran', 38.8, 85]}]}]}


# In[73]:


# ans='Tehran'
d['ab'][3]['Countries'][3]['Iran'][1]


# <h4 align="right">می دانید که در تاپل ها امکان تغییر وجود ندارد. اما من از شما میخواهم که محتوای تاپل زیر را معکوس کنید. لطفا به هر روش ممکن خواسته من را برآورده کنید </h4>
# 

# In[74]:


t = ('Iran' , 'Germany', 'Italy', 'Brazil')


# In[78]:


# ans= ('Brazil', 'Italy', 'Germany', 'Iran')
t[::-1]


# <h4 align="right"> قطعه کدی بنویسید که بررسی کند آیا در رشته زیر کلمه </h4>
# <h4 align="right"> 'cat' </h4>
# <h4 align="right"> وجود دارد یا خیر؟ در صورت وجود کلمه تعداد آن را نمایش دهد.  </h4>
# <h4 align="right"> و در صورت عدم وجود پیغام مناسب را نمایش دهد.  </h4>

# In[79]:


s = 'The cat the best cat in the world. I want to buy this cat '


# In[86]:


# Yes!,  the word 'cat' is in the string
#The count of 'cat' is: 3
a=0
for i in s.split():
    if i=='cat':
        a+=1
if a>=1:
    print('''Yes!,  the word 'cat' is in the string''')
    print('''The count of 'cat' is:''',a)


# <h4 align="right"> کد نوشته شده در قسمت قبل را بر روی رشته زیر امتحان کنید </h4>
# 

# In[90]:


s2 = 'My cats are the bests in the world! '


# In[91]:


#Sorry!,  the word 'cat' is not in the string.

b=0
for i in s2.split():
    if i=='cat':
        b+=1
if b>=1:
    print('''Yes!,  the word 'cat' is in the string''')
    print('''The count of 'cat' is:''',a)
else:
    print('''Sorry!,  the word 'cat' is not in the string.''')


# <h4 align="right"> لیست زیر را به شکل نزولی مرتب کنید </h4>

# In[92]:


lst4 = [100,107,98,112,151, 113,99]


# In[95]:


#[151, 113, 112, 107, 100, 99, 98]

lst4.sort(reverse=True)
lst4


# <h4 align="right"> در دیکشنری زیر اولا دو اشتباه وجود دارد. با استفاده از روش مناسب این اشتباهات را تصحیح کنید.  ثانیا کشور زیر را با پایتخت آن در دیکشنری اضافه نمایید </h4>
# 
# Spain  :  Madrid

# In[106]:


Capitals = {'Iran': 'Tehran', 'Germany': 'Paris', 'France': 'Berlin', 'Italy': 'Rome'}


# In[107]:


Capitals['Germany']='Berlin'
Capitals['France']='Paris'


# In[108]:


#{'Iran': 'Tehran', 'Germany': 'Berlin', 'France': 'Paris', 'Italy': 'Rome'}

Capitals


# In[104]:


Capitals['Spain']='Madrid'


# In[105]:


Capitals


# ### موفق باشید
