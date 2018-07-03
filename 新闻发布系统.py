import pymysql
db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
cursor=db.cursor()
xin_wen_xi_tong = '新闻发布系统'
print(xin_wen_xi_tong.center(70))
def printline():
    print('-'*70)
printline()
while True:
    name = input("请输入你的用户名:")
    sql = "SELECT * FROM user WHERE username='%s'"%name
    a = "SELECT username from user"
    b = cursor.execute(a)
    b = cursor.fetchone()       
    for i in b:
        if name == i:
            passwd = input('请输入密码')
            sql = "SELECT * FROM user WHERE username='%s'"%passwd
            c = "SELECT password from user"
            d = cursor.execute(c)
            d = cursor.fetchone()
            for mima in d:
                if passwd == mima: 
                    print('登录成功')
                    while True: 
                        print("欢迎来到新闻发布系统")
                        print("1 用户管理")
                        print("2 新闻信息")
                        print("3 评论管理")
                        print("4 退出系统")
                        printline()
                        serialn_umber = int(input("请输入操作的序号"))
                        printline()
                        
                        if serialn_umber == 1:
                            print("欢迎进入用户管理")
                            printline()
                            print("1 注册新用户 2 查看新用户 3 修改新用户 4 删除新用户 5 返回主菜单")
                            serialn_umber1 = int(input("请输入操作的序号"))
                            printline()
                            if serialn_umber1 == 1:
                                print("欢迎进入注册用户页面")
                                db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
                                cursor = db.cursor()
                                yong_id = int(input("请输入id号"))
                                name = input("请输入姓名:")
                                age = int(input("请输入年龄:"))
                                zhiwei = input("请输入职位:")
                                sex = input("请输入性别:")
                                charu = "INSERT INTO yonghuguanli VALUES('%d','%s','%d','%s','%s')"%(yong_id,name,age,zhiwei,sex)
                                try:
                                    cursor.execute(charu)
                                    db.commit()
                                    print("注册成功")
                                except:
                                    print("错误")
                                finally:
                                    db.close() 
                            elif serialn_umber1 == 2:
                                print("欢迎进入查看用户页面")
                                db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
                                cursor = db.cursor()
                                yonghu = int(input('请输入查询序号:'))
                                chakan = "SELECT * FROM yonghuguanli WHERE yong_id=%d"%yonghu
                                try:
                                    cursor.execute(chakan)
                                    neirong = cursor.fetchall()
                                    for row in neirong:
                                        yong_id = row[0]
                                        name = row[1]
                                        age = row[2]
                                        zhiwei = row[3]
                                        sex = row[4]
                                        print("yong_id:%d\nname:%s\nage:%d\nzhiwei:%s\nsex:%s\n"%(yong_id,name,age,zhiwei,sex))
                                        db.commit()
                                        print('查询成功')
                                except:
                                    print('错误')

                                finally:
                                    db.close()   
                            elif serialn_umber1 == 3:
                                print("欢迎进入修改用户页面")
                                db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
                                cursor = db.cursor()
                                  
                                print("1 修改名字 2 修改年龄 3 修改职位 4 修改性别")
                                num = int(input('请输入你要修改的序号'))
                                if num == 1:
                                    yong_id = int(input("请输入用户编号:"))
                                    name = input('请输入你要修改的名字')
                                    xiugai = "UPDATE yonghuguanli SET name='%s' WHERE yong_id=%d"%(name,yong_id)
                                elif num == 2:
                                    yong_id = int(input("请输入用户编号:"))
                                    age = int(input('请输入你要修改的年龄'))
                                    xiugai = "UPDATE yonghuguanli SET age=%d WHERE yong_id=%d"%(age,yong_id)
                                elif num == 3:
                                    yong_id = int(input("请输入用户编号:"))
                                    zhiwei = input('请输入你要修改的职位')
                                    xiugai = "UPDATE yonghuguanli SET zhiwei='%s' WHERE yong_id=%d"%(zhiwei,yong_id)
                                elif num == 4:
                                    yong_id = int(input("请输入用户编号:"))
                                    sex = input('请输入你要修改的性别')
                                    xiugai = "UPDATE yonghuguanli SET sex='%s' WHERE yong_id=%d"%(sex,yong_id)
                                try:
                                    cursor.execute(xiugai)
                                    db.commit()
                                    print('修改成功')
                                except:
                                    print("修改失败")
                                finally:
                                    db.close()

                            elif serialn_umber1 == 4:
                                print("欢迎进入删除用户页面")
                                db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
                                cursor = db.cursor()
                                shanchu = int(input("请输入你要删除的序号"))
                                shan = "DELETE FROM yonghuguanli WHERE yong_id=%d"%shanchu
                                try:
                                    cursor.execute(shan)
                                    db.commit()
                                    print('删除成功')
                                except:
                                    print("删除失败")
                                finally:
                                    db.close()
                            e = int(input("返回上一层"))
                            if e == 5:
                                break
                        e = int(input("返回主菜单"))
                        if e==4:
                            print("1 用户管理 2 新闻信息 3 评论管理 4 退出系统")
                            serialn_umber1 = int(input("请输入操作的序号"))
                        elif serialn_umber == 2:
                            print("欢迎进入新闻信息")
                            printline()
                            print("1 添加新闻 2 查看新闻信息 3 修改新闻信息 4 删除新闻信息 5 返回主菜单")
                            serialn_umber2 = int(input("请输入操作的序号"))
                            printline()
                            if serialn_umber2 == 1:
                                print("欢迎进入添加新闻页面")
                                db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
                                cursor = db.cursor()
                                n_id = input("请输入id号:")
                                n_type = input("请输入新闻类型:")
                                n_title = input("请输入新闻标题:")
                                n_content = input("请输入新闻内容:")
                                n_date = input("请输入新闻发布时间:")
                                n_desc = input("请输入新闻描述:")
                                n_rate = input("请输入新闻级别:")
                                n_check = input("请输入新闻是否通过:")
                                tianjia = "INSERT INTO news VALUES('%s','%s','%s','%s','%s','%s','%s','%s')"%(n_id,n_type,n_title,n_content,n_date,n_desc,n_rate,n_check)
                                try:
                                    cursor.execute(tianjia)
                                    db.commit()
                                    print("注册成功")
                                except:
                                    print("错误")
                                finally:
                                    db.close() 
                            elif serialn_umber2 == 2:
                                print("欢迎进入查看新闻信息页面")
                                db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
                                cursor = db.cursor()
                                a = int(input('请输入查询序号:'))
                                chakan = "SELECT * FROM news WHERE n_id=%d"%a
                                try:
                                    cursor.execute(chakan)
                                    neirong = cursor.fetchall()
                                    for row in neirong:
                                        n_id = row[0]
                                        n_type = row[1]
                                        n_title = row[2]
                                        n_content = row[3]
                                        n_date = row[4]
                                        n_desc = row[5]
                                        n_rate = row[6]
                                        n_check = row[7]
                                        print("n_id:%d\nn_type:%s\nn_title:%s\nn_content:%s\nn_date:%s\nn_desc:%s\nn_rate:%d\nn_check:%s\n"%(n_id,n_type,n_title,n_content,n_date,n_desc,n_rate,n_check))
                                        db.commit()
                                        print('查询成功')
                                except:
                                    print('错误')

                                finally:
                                    db.close()   
                            elif serialn_umber2 == 3:
                                print("欢迎进入修改新闻信息页面")
                                db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
                                cursor = db.cursor()
                                  
                                print("1 修改类型 2 修改标题 3 修改内容 4 修改描述信息 5 修改新闻发布时间 6 修改新闻级别 7 修改新闻合格率 ")
                                num = int(input('请输入你要修改的序号'))
                                if num == 1:
                                    n_id = int(input("请输入用户编号:"))
                                    n_type = input('请输入你要修改的新闻类型')
                                    xiugai = "UPDATE news SET n_type='%s' WHERE n_id=%d"%(n_type,n_id)
                                elif num == 2:
                                    n_id = int(input("请输入用户编号:"))
                                    title = input('请输入你要修改的新闻标题')
                                    xiugai = "UPDATE news SET n_title=%s WHERE n_id=%d"%(title,n_id)
                                elif num == 3:
                                    n_id = int(input("请输入用户编号:"))
                                    content = input('请输入你要修改的新闻内容')
                                    xiugai = "UPDATE news SET n_content='%s' WHERE n_id=%d"%(content,n_id)
                                elif num == 4:
                                    n_id = int(input("请输入用户编号:"))
                                    date = input('请输入你要修改的新闻发布时间')
                                    xiugai = "UPDATE news SET n_date='%s' WHERE n_id=%d"%(date,n_id)
                                elif num == 5:
                                    n_id = int(input("请输入用户编号:"))
                                    desc = input('请输入你要修改的新闻描述')
                                    xiugai = "UPDATE news SET n_desc='%s' WHERE n_id=%d"%(desc,n_id)
                                elif num == 6:
                                    n_id = int(input("请输入用户编号:"))
                                    rate = input('请输入你要修改的新闻级别')
                                    xiugai = "UPDATE news SET n_rate='%s' WHERE n_id=%d"%(rate,n_id)
                                elif num == 7:
                                    n_id = int(input("请输入用户编号:"))
                                    check = input('请输入你要修改的新闻合格率')
                                    xiugai = "UPDATE news SET n_check='%s' WHERE n_id=%d"%(check,n_id)
                                try:
                                    cursor.execute(xiugai)
                                    db.commit()
                                    print('修改成功')
                                except:
                                    print("修改失败")
                                finally:
                                    db.close()

                            elif serialn_umber2 == 4:
                                print("欢迎进入删除用户页面")
                                db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
                                cursor = db.cursor()
                                shanchu = int(input("请输入你要删除的序号"))
                                shan = "DELETE FROM news WHERE n_id=%d"%shanchu
                                try:
                                    cursor.execute(shan)
                                    db.commit()
                                    print('删除成功')
                                except:
                                    print("删除失败")
                                finally:
                                    db.close()
                            elif serialn_umber2 == 5:
                                print("1 用户管理 2 新闻信息 3 评论管理 4 退出系统")
                        
                        elif serialn_umber == 3:
                            print("欢迎进入评论管理")
                            printline()
                            print("1 添加评论 2 查看评论 4 删除新用户 5 返回主菜单")
                            serialn_umber1 = int(input("请输入操作的序号"))
                            printline()
                            if serialn_umber1 == 1:
                                print("欢迎进入添加评论页面")
                                db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
                                cursor = db.cursor()
                                p_id = int(input("请输入id号"))
                                p_type = input("请输入评论的类型:")
                                p_content = input("请输入评论内容:")
                                yong_id = input("请输入连接用户管理的id号:")
                                n_id = input("请输入连接新闻信息的id号:")
                                charu = "INSERT INTO ping VALUES('%d','%s','%s','%s','%s')"%(p_id,p_type,p_content,yong_id,n_id)
                                try:
                                    cursor.execute(charu)
                                    db.commit()
                                    print("注册成功")
                                except:
                                    print("错误")
                                finally:
                                    db.close() 
                            elif serialn_umber1 == 2:
                                print("欢迎进入查看用户页面")
                                db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
                                cursor = db.cursor()
                                yonghu = int(input('请输入查询序号:'))
                                chakan = "SELECT * FROM ping WHERE p_id=%d"%yonghu
                                try:
                                    cursor.execute(chakan)
                                    neirong = cursor.fetchall()
                                    for row in neirong:
                                        p_id = row[0]
                                        p_type = row[1]
                                        p_content = row[2]
                                        yong_id = row[3]
                                        n_id= row[4]
                                        print("p_id:%d\np_type:%s\np_content:%s\nyong_id:%d\nn_id:%d\n"%(p_id,p_type,p_content,yong_id,n_id))
                                        db.commit()
                                        print('查询成功')
                                except:
                                    print('错误')

                                finally:
                                    db.close()   
                            elif serialn_umber1 == 4:
                                print("欢迎进入删除用户页面")
                                db = pymysql.connect("localhost","root","bc123","webnews",charset='utf8')
                                cursor = db.cursor()
                                shanchu = int(input("请输入你要删除的序号"))
                                shan = "DELETE FROM ping WHERE p_id=%d"%shanchu
                                try:
                                    cursor.execute(shan)
                                    db.commit()
                                    print('删除成功')
                                except:
                                    print("删除失败")
                                finally:
                                    db.close()
                                    break
                                 
                    def exit():
                        print("退出系统")
                            

           
                            
          
