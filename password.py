password = "a123456"
num = 3
user = input ("请输入您的密码：")
if user == password:
    print ("登入成功！")
else:
    
    while num > 1:
        num = num - 1
        print ("密码错误！还有",num,"次机会")
        user = input ("请输入您的密码：")
    while num == 1:
        print ("密码错误！还有0次机会")
        break
