def abc_md5(abc):
    '''
    加密用户输入过来的密码
    param abc
    return
    '''
    # 调md5方法
    h1 = hashlib.md5()
    h1.update(abc.encode(encoding='utf-8'))# 解码成字节码
    return h1.hexdigest()
username = 'oldboy'
abc = '112233'
abc = abc_md5(abc)#调用MD5加密，密码md5加密的密码是不能解码的，但是撞库可以解密
i = 1
while i <= 3:
    username1 = input('请输入用户名:')
    abc1 = input('请输入用户密码:')
    abc1 = abc_md5(abc1)
    if username == username1 and abc1 == abc:
        print('------登入成功------')
        while i <= 3:
            msg = ['取款', '查询余额', '转账', '存款']
            for i ,j in enumerate(msg): #把列表转字典的形式，读取索引和值
                print(i+1, j)
            gn1 = input('请按照上面的功能列表输入数字1、2、3、4执行功能或输入y(退出):')
            if gn1 == 'y':
                print('用户退出')
                i = 4
            else:
                try:
                    gn = int(gn1)-1
                    if gn1 not in ['1', '2', '3', '4']:
                        raise IOError
                except ValueError:
                    print('请输入1-4的数字指定功能')
                except IOError:
                    print('请输入的数字超出范围没有这个功能，请输入范围内的功能')
                else:
                    print('正在执行{0}......'.format(msg[gn]))
    else:
        i += 1
        if i > 3:
            print('你的密码输入错误三次已被机器没收，请联系相关人员')
