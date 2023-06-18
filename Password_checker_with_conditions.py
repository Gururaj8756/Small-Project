import re
password=input("Enter Passwords: ").split(',')
lst=[]
#Contains 6-12 char,one upper case as well as lower case conatins at least one digit 
# And have a symnols from @#$
for i in password:
    count=0
    count+=bool(6<=len(i)<=12)
    count+=bool(re.search("[a-z]",i))
    count+=bool(re.search("[A-Z]",i))
    count+=bool(re.search("[0-9]",i))
    count+=bool(re.search("[@#$]",i))
    if count==5:
        lst.append(i)

print(','.join(lst))