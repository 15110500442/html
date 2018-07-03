while True:
    print("1 用户管理 2 管理员管理 3 权限管理 4 新闻管理 5 评论管理 6 退出系统")
    printline()
    serialn_umber = int(input("请输入操作的序号"))
    printline()
    while True:
        if serialn_umber == 1:
    	    print("1 注册新用户 2 查看新用户 3 修改新用户")
    	    serialn_umber1 = int(input("请输入操作的序号"))
    	    if serialn_umber1 == 1:
    	        print("注册新用户")
    	        pass
    	    elif serialn_umber1 == 2:
                print("查看新用户")
                pass


        if serialn_umber == 2:
    	    print("管理员管理")
        if serialn_umber == 3:
    	    print("权限管理")
        if serialn_umber == 4:
           print("新闻管理")
        if serialn_umber == 5:
    	    print("评论管理")
        if serialn_umber == 6:
    	    print("退出系统")
    	    break










