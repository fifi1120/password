password = "a123456"
num = 3 #剩余机会

while num > 0:
    user = input ("请输入您的密码：")
    if user == password:
        print ("登入成功！")
        break  #逃出回圈
    else:
        num = num - 1
        print ("密码错误！还有",num,"次机会")
        if num == 0:
            break
