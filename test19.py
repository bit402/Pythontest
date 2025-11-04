while True:
    print("[1]使用用户名登陆")
    print("[2]使用手机号登录")
    print("[0]退出登陆系统")
    choice = input("请选择:")
    if(choice.isdigit()):
        choice = int(choice)
        match (choice):
            case 1:
                name = input("请输入用户名（用户名必须全部是小写，首字母不能为数字，长度必须为6位以上）：")
                if (name.islower() and len(name) >= 6 and (not (name[0].isdigit()))):
                    password = input("请输入6位数字的密码：")
                    if len(password) == 6:
                        if (name == "admin123" and password == "200325"):
                            print("登陆成功！")
                            break
                        else:
                            print("对不起，用户名或者密码错误，请重试！")
                    else:
                        print("对不起，密码的长度不合法，请重试！")
                elif (name[0].isdigit()):
                    print("对不起，用户名的首字母不能为数字！")
                elif not (name.islower()):
                    print("对不起，用户名必须全部为小写")
                elif (len(name) < 6):
                    print("对不起，用户名的长度必须为6位以上！")
            case 2:
                phone = input("请输入您的手机号：")
                if (phone.isdigit() and len(phone) == 11):
                    password = input("请输入密码：")
                    if len(password) == 6:
                        if (phone == "15811119999" and password == "200325"):
                            print("登陆成功！")
                            break
                        else:
                            print("对不起，手机号或者密码有误，请重新登录！")
                    else:
                        print("对不起，密码的长度不合法，请重试！")
                elif (not (phone.isdigit())):
                    print("对不起，手机号应为纯数字组成")
                elif (len(phone) != 11):
                    print("对不起，手机号的长度应为11位！")
            case 0:
                print("退出登陆系统！")
                break
            case _:
                print("对不起输入不合法，请按照功能编号输入对应的数字！")
    else:
        print("对不起输入不合法，请按照功能编号输入对应的数字！")