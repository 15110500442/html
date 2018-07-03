#python版支付宝管理系统v1.0
#首先是进入支付宝的注册和登录功能
zhi_fu_bao ='欢迎使用支付宝'
#做一个空列表来装修改信息
he_zi = []
print(zhi_fu_bao.center(50))
#存有字典的列表
account_passwd = []
#来储存帐号密码
list_account = []
#用函数定义一个*组成的横线
def printline():
    print('*'*50)
printline()
while True:
    
    print('1 注册帐号，2 登录帐号')
    printline()
    denglu_zhuce = int(input('请输入你要选择的功能序号'))
           
    #设置个人信息
    def she_zhi():
        name = input('请输入姓名')
        age = int(input('请输入年龄'))
        xueid = input('请输入学历')
        di_qu = input('请输入地区')
        tel = int(input('请输入手机号'))
        height = float(input('请输入身高'))
        weight = float(input('请输入体重'))
        xing_zuo = input('请输入星座')
        zhi_ye = input('请输入职业')
        money = float(input('请输入收入'))
        ai_hao = input('请输入兴趣爱好')
        #所有的个人信息
        xin_xi = {'姓名':name,'年龄':age,'学历':xueid,'地区':di_qu,'手机号':tel,'身高':height,'体重':weight,'星座':xing_zuo,'职业':zhi_ye,'收入':money,'兴趣爱好':ai_hao}
        he_zi.append(xin_xi)
        print('*'*50)
        print('现在个人信息有%s'%he_zi)
        xx = input('是否退出y/n')
        if xx == 'n':
            print('1为设置个人信息,2为修改个人信息,3为身份验证,4为选择应用服务,5为退出系统')
            choose = int(input('请输入您的选择'))
            if choose == 1:
                she_zhi()
            elif choose == 2:
                xiu_gai()
            elif choose == 3:
                yan_zheng()
            elif choose == 4:
                ying_yong()
            elif choose == 5:
                exit()
            
    #修改个人信息    
    def xiu_gai():
        printline()
        print("修改个人信息")
        name = input('请输入你要修改的名字')
        for dic in he_zi:
            count = 0 
            if dic['姓名']==name:
                he_zi[count]['姓名']=input('请输入姓名')
                he_zi[count]['年龄']=int(input('请输入年龄'))
                he_zi[count]['学历']=input('请输入学历')
                he_zi[count]['地区']=input('请输入地区')
                he_zi[count]['手机号']=int(input('请输入手机号'))
                he_zi[count]['身高']=float(input('请输入身高'))
                he_zi[count]['体重']=float(input('请输入体重'))
                he_zi[count]['星座']=input('请输入星座')
                he_zi[count]['职业']=input('请输入职业')
                he_zi[count]['收入']=float(input('请输入收入'))
                he_zi[count]['兴趣爱好']=input('请输入兴趣爱好')
            else:
                count +=1
        print('修改后的结果是%s'%he_zi)       
        printline()
        
        print('1为设置个人信息,2为修改个人信息,3为身份验证,4为选择应用服务,5为退出系统')
        choose = int(input('请输入您的选择'))
        if choose == 1:
            she_zhi()
        elif choose == 2:
            xiu_gai()
        elif choose == 3:
            yan_zheng()
        elif choose == 4:
            ying_yong()
        elif choose == 5:
            exit()
        yan_zheng() 
    
    #身份验证
    def yan_zheng():
        guo_ji = input('请输入国籍')
        name = input('请输入姓名')
        #证件类型
        zjbype = input('请输入证件类型')
        id_cord = input('请输入证件号码')
        di_qu = input('请输入所在地区')
        addr = input('请输入详细地址')
        print('身份验证成功')
        print('1为设置个人信息,2为修改个人信息,3为身份验证,4为选择应用服务,5为退出系统')
        choose = int(input('请输入您的选择'))
        if choose == 1:
            she_zhi()
        elif choose == 2:
            xiu_gai()
        elif choose == 3:
            yan_zheng()
        elif choose == 4:
            ying_yong()
        elif choose == 5:
            exit()
        ying_yong()
        
            
    #选择支付宝应用
    def ying_yong():
        while True:
            print('1 充值中心 2 信用卡还款 3 生活缴费 4 转账 5 蚂蚁借呗 6 人脸识别 7 共享单车 8发票管家 9 退出选择应用')
            printline()
            name = int(input('请输入你要选择的支付宝应用程序'))
            if name == 1:
                print('充值中心')
                tel = int(input('请输入手机号码:'))
                money = int(input('请输入充值金额50 100 150:'))
                if money == 50:
                    print('充值成功')
                    printline()
                elif money == 100:
                    print('充值成功')
                    printline()
                elif money == 150:
                    print('充值成功')
                    printline()
                else:
                    print('系统出现错误，请稍后重试')
                
                    printline()
            elif name == 2:
                print('信用卡还款')
                yin_hang = int(input('请添加信用卡:'))
                yin_hang = input('请输入发卡银行:')
                name = input('请输入持卡人姓名:')
                ti_xin = input('是否开通还款提醒:')
                print('添加信用卡成功:')
                printline()#一个函数等于横线
                ka_hao = int(input('请输入信用卡卡号:'))
                money = int(input('请输入还款金额:'))
                print('还款成功')
                printline()
            elif name == 3:
                print('生活缴费')
                bype = input('请输入缴费类型 电费 水费 燃气费 物业费:')
                if bype == '电费':
                    biao_hao = int(input('请输入电卡编号'))
                    money = int(input('请输入缴费金额'))
                    print('缴费成功')
                    printline()
                elif bype == '水费':
                    ji_gou = int(input('请输入机构'))
                    money = int(input('请输入缴费金额'))
                    print('缴费成功')
                    printline()
                elif bype == '燃气费':
                    ji_gou = int(input('请输入机构'))
                    money = int(input('请输入缴费金额'))
                    print('缴费成功')
                    printline()
                elif bype == '物业费':
                    ji_gou = int(input('请输入机构'))
                    money = int(input('请输入缴费金额'))
                    print('缴费成功')
                    printline()
                else:
                    print('系统正在升级，请稍后重试')
                    printline()

            elif name == 4:
                print('转账')
                bype = input('请输入转账方式 我的朋友 支付宝账户 银行卡:')
                if bype == '我的朋友':
                    tian_jia = int(input('请输入添加朋友的支付宝号'))
                    print('添加成功')
                    money = int(input('请输入转账金额'))
                    print('转账成功')
                    printline()
                elif bype == '支付宝号':
                    account = int(input('请输入对方的帐号'))
                    money = int(input('请输入转账金额'))
                    print('转账成功')
                    printline()
                elif bype == '银行卡':  
                    account = int(input('请输入对方的银行卡号'))
                    money = int(input('请输入转账金额'))
                    print('转账成功')
                    printline()
                else:
                    print('系统正在升级，请重试')
            elif name == 5:
                print('蚂蚁借呗')
                money = int(input('请输入你的借呗总金额'))
                jie_money = int(input('请输入你要借出的资金'))
                date = int(input('请输入你要借款期限'))
                li_xi = (jie_money * date) * 0.0005
                print('借款成功')
                print('利息为%s元'%li_xi)
                printline()
            elif name == 6:
                print('人脸识别')
                bype = input('请输入类型(刷脸支付  刷脸看运势)')
                if bype == '刷脸支付':
                    kai_tong = input('请输入是否立即开通刷脸支付')
                    if kai_tong == '是':
                        print('您已开通刷脸服务，可在线下店铺实现刷脸买单无需手机')
                        printline()
                    else:
                        print('')
                        printline()
                elif bype == '刷脸看运势':
                    lian = input('请把脸放在框内保持不动')
                    print('刷脸通过')
                    print('今天的运势:运势很好，人见人爱，花见花开，情商大增')
                    printline()
            elif name == 7:
                print('共享单车')
                bype = int(input('请输入单车的名字(小黄车  优拜单车)'))
                if bype == '小黄车':
                    jin_ru = input('是否进入小黄车界面')
                    if jin_ru == '是':
                        print('进入界面，扫码骑行')
                    else:
                        print('退出')
                        printline()
                if bype == '优拜单车':
                    jin_ru = input('是否进入优拜单车界面')
                    if jin_ru == '是':
                        print('进入界面，扫码骑行')
                    else:
                        print('退出')
                        printline()
            elif name == 8:
                print('发票管家')
                bype = int(input('请输入发票类型(1 发票摇奖，2 发票代开)'))
                if bype == 1:
                    dai_ma = int(input('请输入发票代码'))
                    num = int(input('请输入发票号码'))
                    money = int(input('请输入发票金额'))
                    date = int(input('请输入开票日期'))
                    lei_xing = int(input('请输入发票类型(1 增值税普通发票 2 增值税电子普通发票 3 增值税普通发票(卷式))'))
                    addr = int(input('请输入发票归属地'))
                    print('开始摇奖')
                    print('恭喜你荣获特等奖，奖品是人民币10000元')
                    
                else:
                    print('不好意思，机会与你插肩而过')
                
                    break
                    printline()
                    
                if bype == 2:
                    cheng_shi = int(input('请输入代开发票的城市'))
                    fu_wu_shang = int(input('请输入服务商'))
                    print('立即申请')
                    print('恭喜你申请成功')
                else:
                    print('很抱歉，申请失败')
                    printline()
  
            elif name == 9:
                print('退出选择系统')
                
                print('1为设置个人信息,2为修改个人信息,3为身份验证,4为选择应用服务,5为退出系统')
                choose = int(input('请输入您的选择'))
                if choose == 1:
                    she_zhi()
                elif choose == 2:
                    xiu_gai()
                elif choose == 3:
                    yan_zheng()
                elif choose == 4:
                    ying_yong()
                elif choose == 5:
                    exit()
            
                
               
                break
    #退出支付宝
    def exit():
        print('退出,欢迎下次使用')
          
          
    def zhu_ce():
        print('开始注册')
        name = input('请输入你要注册的帐号')
    #注册的时候不能出现重名，所以用for来筛选重名
        for dic in account_passwd:
            list_account.append(dic['name'])
        if name in list_account:
            print('帐号已经存在')
        elif name not in list_account:
            passwd = input('请输入你的注册密码')
        #创建一个临时字典让储存帐号和密码
            ling_shi = {}
            ling_shi['name'] = name
            ling_shi['passwd'] = passwd
            account_passwd.append(ling_shi)
            print('注册成功')
            print(account_passwd)
            deng_lu()
            
    #登录
    def deng_lu():
        print('准备登录')
        name = input('请输入帐号')
            #判断帐号是否存在
        for dic in account_passwd:
            list_account.append(dic['name'])
            print(list_account)
        if name not in list_account:
            print('帐号不存在，请先注册')
        elif name in list_account:
            mima = input('请输入密码:')
            a = list_account.index(name)
            b = account_passwd[int(a)]
            if mima == b['passwd']:
                print('登录成功')
                  
                print('1为设置个人信息,2为修改个人信息,3为身份验证,4为选择应用服务,5为退出系统')
                choose = int(input('请输入您的选择'))
                if choose == 1:
                    she_zhi()
                elif choose == 2:
                    xiu_gai()
                elif choose == 3:
                    yan_zheng()
                elif choose == 4:
                    ying_yong()
                elif choose == 5:
                    exit()
            else:
                print('密码错误')
    if denglu_zhuce == 1 :
        zhu_ce()
    if denglu_zhuce == 2:
        deng_lu()
    break     
