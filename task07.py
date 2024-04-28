#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
import pymysql
from tkinter import ttk

# 打开数据库连接
def Sql_link():
    #生成数据库
    db = pymysql.connect(host='localhost',user='root',password='321',database='library')
    # 使用 cursor() 方法创建一个游标对象
    cursor = db.cursor()
    return db,cursor

class Manager:
    # 用户注册
    def create_client(self):
        # 创建窗口
        create_client_root = Tk()
        create_client_root.title("用户创建")
        create_client_root.config(width=600)
        create_client_root.config(height=600)
        # 定义关联变量
        client_id = StringVar(create_client_root, value='')
        client_code = StringVar(create_client_root, value='')
        client_rate = StringVar(create_client_root, value='')
        # 提示性标签
        labelclient_id = Label(create_client_root, text="用户ID注册", font=("微软雅黑 -20"))
        labelclient_code = Label(create_client_root, text="用户密码设置", font=("微软雅黑 -20"))
        labelclient_rate = Label(create_client_root, text="用户积分设置", font=("微软雅黑 -20"))
        # 设定标签位置
        labelclient_id.place(x=200, y=100, height=40, width=200)
        labelclient_code.place(x=200, y=200, height=40, width=200)
        labelclient_rate.place(x=200, y=300, height=40, width=200)
        # 定义录入信息文本框,以关联变量形式存储
        entryclient_id = Entry((create_client_root), textvariable=client_id)
        entryclient_id.place(x=200, y=150, height=40, width=200)
        entryclient_code = Entry((create_client_root), textvariable=client_code)
        entryclient_code.place(x=200, y=250, height=40, width=200)
        entryclient_rate = Entry((create_client_root), textvariable=client_rate)
        entryclient_rate.place(x=200, y=350, height=40, width=200)

        # 录入信息回调函数
        def Button_Ok():
            # 设置标志位判断是否存在ID重复
            flag = 0
            # 连接数据库
            db, cur = Sql_link()
            # 将得到的StringVar对象传值回来
            data_client_id = str(entryclient_id.get())
            data_client_code = str(entryclient_code.get())
            data_client_rate = str(entryclient_rate.get())
            # 判断是否ID重复
            search = cur.execute("SELECT * FROM client WHERE id =  " + data_client_id + ';')
            if (search > 0):
                flag = 1
            else:
                flag = 0
            if (flag == 0):
                try:
                    # 写入数据
                    sql1 = "INSERT INTO client(id,code,rate)"
                    sql1 += "VALUES('%s','%s','%s')" % (data_client_id, data_client_code,data_client_rate)
                    cur.execute(sql1)
                    db.commit()
                    messagebox.showinfo(title="恭喜", message="注册成功！！！")
                    create_client_root.destroy()
                except:
                    messagebox.showerror(message="注册失败！！！")
            else:
                messagebox.showerror("该用户名已注册！！！")

        # 确认以及退出按钮
        Ok_Button = Button(create_client_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
        Exit_Button = Button(create_client_root, text="退出", font=("微软雅黑 -20"), command=create_client_root.destroy)
        Ok_Button.place(x=75, y=450, height=40, width=200)
        Exit_Button.place(x=325, y=450, height=40, width=200)
    # 添加书籍
    def insert_book(self):
        # 创建窗口
        insert_book_root = Tk()
        insert_book_root.title("添加书籍")
        insert_book_root.config(width=600)
        insert_book_root.config(height=800)
        # 定义关联变量
        book_id = StringVar(insert_book_root, value='')
        book_name = StringVar(insert_book_root, value='')
        book_author = StringVar(insert_book_root, value='')
        book_type = StringVar(insert_book_root, value='')
        book_state = StringVar(insert_book_root, value='')
        book_storge = StringVar(insert_book_root, value='')
        # 提示性标签
        labelbook_id = Label(insert_book_root, text="书籍id", font=("微软雅黑 -20"))
        labelbook_name = Label(insert_book_root, text="书籍名称", font=("微软雅黑 -20"))
        labelbook_author = Label(insert_book_root, text="书籍作者", font=("微软雅黑 -20"))
        labelbook_type = Label(insert_book_root, text="书籍种类", font=("微软雅黑 -20"))
        labelbook_state = Label(insert_book_root, text="书籍状态", font=("微软雅黑 -20"))
        labelbook_storge = Label(insert_book_root, text="书籍库存", font=("微软雅黑 -20"))
        # 设定标签位置
        labelbook_id.place(x=200, y=30, height=40, width=200)
        labelbook_name.place(x=200, y=130, height=40, width=200)
        labelbook_author.place(x=200, y=230, height=40, width=200)
        labelbook_type.place(x=200, y=330, height=40, width=200)
        labelbook_state.place(x=200, y=430, height=40, width=200)
        labelbook_storge.place(x=200, y=530, height=40, width=200)
        # 定义录入信息文本框,以关联变量形式存储
        entrybook_id = Entry((insert_book_root), textvariable=book_id)
        entrybook_id.place(x=200, y=80, height=40, width=200)
        entrybook_name = Entry((insert_book_root), textvariable=book_name)
        entrybook_name.place(x=200, y=180, height=40, width=200)
        entrybook_author = Entry((insert_book_root), textvariable=book_author)
        entrybook_author.place(x=200, y=280, height=40, width=200)
        entrybook_type = Entry((insert_book_root), textvariable=book_type)
        entrybook_type.place(x=200, y=380, height=40, width=200)
        entrybook_state = Entry((insert_book_root), textvariable=book_state)
        entrybook_state.place(x=200, y=480, height=40, width=200)
        entrybook_storge = Entry((insert_book_root), textvariable=book_storge)
        entrybook_storge.place(x=200, y=580, height=40, width=200)

        # 录入信息回调函数
        def Button_Ok():
            # 设置标志位判断是否存在ID重复
            flag = 0
            # 连接数据库
            db, cur = Sql_link()
            # 将得到的StringVar对象传值回来
            data_book_id = str(entrybook_id.get())
            data_book_name = str(entrybook_name.get())
            data_book_author = str(entrybook_author.get())
            data_book_type = str(entrybook_type.get())
            data_book_state = str(entrybook_state.get())
            data_book_storge = str(entrybook_storge.get())
            # 判断是否信息重复
            search1 = cur.execute("SELECT * FROM book WHERE name = '%s'" % data_book_name)
            search2 = cur.execute("SELECT * FROM book WHERE author = '%s'" % data_book_author)
            if (search1 > 0 and search2 > 0):
                flag = 1
            else:
                flag = 0
            if (flag == 0):
                try:
                    # 写入数据
                    sql1 = "INSERT INTO book(id,name,author,type,state,storge)"
                    sql1 += "VALUES('%s','%s','%s','%s','%s','%s')" % (
                    data_book_id, data_book_name, data_book_author, data_book_type, data_book_state, data_book_storge)
                    cur.execute(sql1)
                    db.commit()
                    messagebox.showinfo(title="恭喜", message="录入成功！！！")
                    insert_book_root.destroy()
                except:
                    messagebox.showerror(message="ID重复！！！")
            else:
                # 查找对应的ID号
                sql2 = "UPDATE book SET storge = storge + %d WHERE name = '%s'" % (
                eval(data_book_storge), data_book_name)
                cur.execute(sql2)
                db.commit()
                messagebox.showinfo(title="恭喜", message="录入成功！！！")

        # 确认以及退出按钮
        Ok_Button = Button(insert_book_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
        Exit_Button = Button(insert_book_root, text="退出", font=("微软雅黑 -20"), command=insert_book_root.destroy)
        Ok_Button.place(x=75, y=650, height=40, width=200)
        Exit_Button.place(x=325, y=650, height=40, width=200)
    # 按作者筛选书籍
    def sort_by_author(self):
            sort_by_author_root = Tk()
            sort_by_author_root.title("按作者分类")
            sort_by_author_root.config(width=600)
            sort_by_author_root.config(height=600)
            # 创建树对象用于展示数据
            book_tree = ttk.Treeview(sort_by_author_root, height=30, columns=['1', '2', '3', '4', '5', '6'],
                                     show='tree headings')
            book_tree.column('1', width=100, anchor='center')
            book_tree.column('2', width=100, anchor='center')
            book_tree.column('3', width=100, anchor='center')
            book_tree.column('4', width=100, anchor='center')
            book_tree.column('5', width=100, anchor='center')
            book_tree.column('6', width=100, anchor='center')
            # 设置树的表头
            book_tree.heading('1', text='ID')
            book_tree.heading('2', text='NAME')
            book_tree.heading('3', text='作者')
            book_tree.heading('4', text='类型')
            book_tree.heading('5', text='状态')
            book_tree.heading('6', text='库存')
            try:
                db, cur = Sql_link()
                sql = "SELECT * FROM book ORDER BY author DESC"
                cur.execute(sql)
                db.commit()
                # 给树各项参数赋值，若为NONE值则break
                for i in range(0, 30):
                    results = cur.fetchone()
                    while (results):
                        book_tree.insert('', i, values=results)
                        break
            except:
                messagebox.showerror(message="排序失败!")
            book_tree.pack()

            Exit_Button = Button(sort_by_author_root, text="退出", font=("微软雅黑 -20"), command=sort_by_author_root.destroy)
            Exit_Button.place(x=350, y=530, height=40, width=200)
    # 按题材筛选书籍
    def sort_by_type(self):
            sort_by_type_root = Tk()
            sort_by_type_root.title("按种类分类")
            sort_by_type_root.config(width=600)
            sort_by_type_root.config(height=600)
            # 创建树对象用于展示数据
            book_tree = ttk.Treeview(sort_by_type_root, height=30, columns=['1', '2', '3', '4', '5', '6'],
                                     show='tree headings')
            book_tree.column('1', width=100, anchor='center')
            book_tree.column('2', width=100, anchor='center')
            book_tree.column('3', width=100, anchor='center')
            book_tree.column('4', width=100, anchor='center')
            book_tree.column('5', width=100, anchor='center')
            book_tree.column('6', width=100, anchor='center')
            # 设置树的表头
            book_tree.heading('1', text='ID')
            book_tree.heading('2', text='NAME')
            book_tree.heading('3', text='作者')
            book_tree.heading('4', text='类型')
            book_tree.heading('5', text='状态')
            book_tree.heading('6', text='库存')
            try:
                db, cur = Sql_link()
                sql = "SELECT * FROM book ORDER BY type DESC"
                cur.execute(sql)
                db.commit()
                # 给树各项参数赋值，若为NONE值则break
                for i in range(0, 30):
                    results = cur.fetchone()
                    while (results):
                        book_tree.insert('', i, values=results)
                        break
            except:
                messagebox.showerror(message="排序失败!")
            book_tree.pack()

            Exit_Button = Button(sort_by_type_root, text="退出", font=("微软雅黑 -20"), command=sort_by_type_root.destroy)
            Exit_Button.place(x=350, y=530, height=40, width=200)
    # 书籍管理
    def book_menu(self):
        # 创建窗口
        book_menu_root = Tk()
        book_menu_root.title("功能菜单")
        book_menu_root.config(width=600)
        book_menu_root.config(height=600)
        # 删除书籍
        def delete_book():
            # 创建窗口
            delete_book_root = Tk()
            delete_book_root.title("书籍信息删除")
            delete_book_root.config(width=600)
            delete_book_root.config(height=600)

            book_name = StringVar(delete_book_root, value='')
            # 提示性标签
            labelbook_name = Label(delete_book_root, text="要删除的书籍id", font=("微软雅黑 -20"))
            entrybook_name = Entry(delete_book_root, textvariable=book_name)

            labelbook_name.place(x=200, y=100, height=40, width=200)
            entrybook_name.place(x=200, y=200, height=40, width=200)

            def Button_Ok():
                db, cur = Sql_link()
                book_name = eval(entrybook_name.get())
                # 查找对应的书籍
                sql = "SELECT * FROM book WHERE id = %s" % (book_name)
                search = cur.execute(sql)
                if (search > 0):
                    messagebox.showinfo(message="删除成功!")
                    # 删除目标行
                    sql1 = "DELETE FROM book WHERE id = %s" % (book_name)
                    cur.execute(sql1)
                    db.commit()
                else:
                    messagebox.showerror(message="该书籍不存在!")

            Ok_Button = Button(delete_book_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
            Exit_Button = Button(delete_book_root, text="退出", font=("微软雅黑 -20"), command=delete_book_root.destroy)
            Ok_Button.place(x=75, y=350, height=40, width=200)
            Exit_Button.place(x=325, y=350, height=40, width=200)

        # 设置按钮
        button_book1 = Button(book_menu_root, text="按作者分类", font=("微软雅黑 -20"), command=self.sort_by_author)
        button_book2 = Button(book_menu_root, text="按题材分类", font=("微软雅黑 -20"), command=self.sort_by_type)
        button_book3 = Button(book_menu_root, text="书籍删除", font=("微软雅黑 -20"), command=delete_book)
        button_book4 = Button(book_menu_root, text="书籍录入", font=("微软雅黑 -20"), command=self.insert_book)
        button_book1.place(x=200, y=30, height=40, width=200)
        button_book2.place(x=200, y=130, height=40, width=200)
        button_book3.place(x=200, y=230, height=40, width=200)
        button_book4.place(x=200, y=330, height=40, width=200)

        Exit_Button = Button(book_menu_root, text="退出", font=("微软雅黑 -20"), command=book_menu_root.destroy)
        Exit_Button.place(x=200, y=430, height=40, width=200)
    # 用户信息修改
    def edit_client(self):
        # 创建窗口
        show_edit_client_root = Tk()
        show_edit_client_root.title("功能菜单")
        show_edit_client_root.config(width=600)
        show_edit_client_root.config(height=600)

        def client_info():
            client_info_root = Tk()
            client_info_root.title("用户信息")
            client_info_root.config(width=600)
            client_info_root.config(height=600)
            # 创建树对象用于展示数据
            client_info_tree = ttk.Treeview(client_info_root, height=30, columns=['1', '2', '3'],
                                     show='tree headings')
            client_info_tree.column('1', width=100, anchor='center')
            client_info_tree.column('2', width=100, anchor='center')
            client_info_tree.column('3', width=100, anchor='center')
            # 设置树的表头
            client_info_tree.heading('1', text='ID')
            client_info_tree.heading('2', text='CODE')
            client_info_tree.heading('3', text='RATE')
            try:
                db, cur = Sql_link()
                sql = "SELECT * FROM client ORDER BY rate DESC"
                cur.execute(sql)
                db.commit()
                # 给树各项参数赋值，若为NONE值则break
                for i in range(0, 30):
                    results = cur.fetchone()
                    while (results):
                        client_info_tree.insert('', i, values=results)
                        break
            except:
                messagebox.showerror(message="排序失败!")
            client_info_tree.pack()

            Exit_Button = Button(client_info_root, text="退出", font=("微软雅黑 -20"), command=client_info_root.destroy)
            Exit_Button.place(x=100, y=530, height=40, width=200)
        def delete_client():
            delete_client_root = Tk()
            delete_client_root.title("用户删除")
            delete_client_root.config(width=600)
            delete_client_root.config(height=600)
            # 定义关联变量
            client_id = StringVar(delete_client_root, value='')
            # 提示性标签
            labelclient_id = Label(delete_client_root, text="用户ID", font=("微软雅黑 -20"))
            # 设定标签位置
            labelclient_id.place(x=200, y=150, height=40, width=200)
            # 定义录入信息文本框,以关联变量形式存储
            entryclient_id = Entry(delete_client_root, textvariable=client_id)
            entryclient_id.place(x=200, y=200, height=40, width=200)

            def Button_Ok():
                db, cur = Sql_link()
                client_id = eval(entryclient_id.get())
                sql = "DELETE FROM client WHERE ID = %d" % (client_id)
                try:
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo(message="删除成功!")
                except:
                    messagebox.showerror(message="删除失败!")

            Ok_Button = Button(delete_client_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
            Exit_Button = Button(delete_client_root, text="退出", font=("微软雅黑 -20"), command=delete_client_root.destroy)
            Ok_Button.place(x=75, y=300, height=40, width=200)
            Exit_Button.place(x=325, y=300, height=40, width=200)
        def change_code():
            # 创建窗口
            change_code_root = Tk()
            change_code_root.title("用户密码修改")
            change_code_root.config(width=600)
            change_code_root.config(height=600)

            client_name = StringVar(change_code_root, value='')
            old_client_code = StringVar(change_code_root, value='')

            # 提示性标签
            labelclient_name = Label(change_code_root, text="要修改的用户ID", font=("微软雅黑 -20"))
            entryclient_name = Entry(change_code_root, textvariable=client_name)
            labelold_client_code = Label(change_code_root, text="请输入原密码", font=("微软雅黑 -20"))
            entryold_client_code = Entry(change_code_root, textvariable=old_client_code)

            labelclient_name.place(x=200, y=50, height=40, width=200)
            entryclient_name.place(x=200, y=150, height=40, width=200)
            labelold_client_code.place(x=200, y=250, height=40, width=200)
            entryold_client_code.place(x=200, y=350, height=40, width=200)

            def Button_Ok():
                db, cur = Sql_link()
                client_name = str(entryclient_name.get())
                old_client_code = entryold_client_code.get()
                # 匹配对应的ID
                sql = "SELECT * FROM client WHERE id=%s AND code='%s'" % (client_name, old_client_code)
                search = cur.execute(sql)
                if (search > 0):

                    def Button_Ok():
                        try:
                            new_client_code = entrynew_client_code.get()
                            messagebox.showinfo(message="修改成功!")
                            # 利用UPDATE来修改密码
                            sql1 = "UPDATE client SET code = '%s' WHERE id = '%s'" % (new_client_code, client_name)
                            cur.execute(sql1)
                            db.commit()
                        except:
                            messagebox.showerror(message="修改失败!")
                    # 创建新窗口
                    input_code_root = Tk()
                    input_code_root.title("用户密码修改")
                    input_code_root.config(width=600)
                    input_code_root.config(height=600)
                    # 设置关联变量
                    new_client_code = StringVar(input_code_root, value='')
                    labelnew_client_code = Label(input_code_root, text="新的密码", font=("微软雅黑 -20"))
                    entrynew_client_code = Entry(input_code_root, textvariable=new_client_code)
                    # 设置提示性标签
                    labelnew_client_code.place(x=200, y=200, height=40, width=200)
                    entrynew_client_code.place(x=200, y=300, height=40, width=200)
                    Ok_Button = Button(input_code_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
                    Exit_Button = Button(input_code_root, text="退出", font=("微软雅黑 -20"), command=input_code_root.destroy)
                    Ok_Button.place(x=75, y=450, height=40, width=200)
                    Exit_Button.place(x=325, y=450, height=40, width=200)
                else:
                    messagebox.showerror(message="该用户不存在或密码错误!")

            Ok_Button = Button(change_code_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
            Exit_Button = Button(change_code_root, text="退出", font=("微软雅黑 -20"), command=change_code_root.destroy)
            Ok_Button.place(x=75, y=450, height=40, width=200)
            Exit_Button.place(x=325, y=450, height=40, width=200)
        # 设置按钮
        button_client1 = Button(show_edit_client_root, text="用户信息", font=("微软雅黑 -20"), command=client_info)
        button_client2 = Button(show_edit_client_root, text="账户删除", font=("微软雅黑 -20"), command=delete_client)
        button_client3 = Button(show_edit_client_root, text="密码修改", font=("微软雅黑 -20"), command=change_code)
        button_client1.place(x=200, y=130, height=40, width=200)
        button_client2.place(x=200, y=230, height=40, width=200)
        button_client3.place(x=200, y=330, height=40, width=200)

        Exit_Button = Button(show_edit_client_root, text="退出", font=("微软雅黑 -20"), command=show_edit_client_root.destroy)
        Exit_Button.place(x=200, y=430, height=40, width=200)
    # 用户积分修改
    def rate_menu(self):
        rate_menu_root = Tk()
        rate_menu_root.title("用户积分修改")
        rate_menu_root.config(width=600)
        rate_menu_root.config(height=600)
        # 定义关联变量
        client_id = StringVar(rate_menu_root, value='')
        client_rate = StringVar(rate_menu_root, value='')
        # 提示性标签
        labelclient_id = Label(rate_menu_root, text="用户ID", font=("微软雅黑 -20"))
        labelclient_rate = Label(rate_menu_root, text="积分数", font=("微软雅黑 -20"))
        # 设定标签位置
        labelclient_id.place(x=200, y=50, height=40, width=200)
        labelclient_rate.place(x=200, y=150, height=40, width=200)
        # 定义录入信息文本框,以关联变量形式存储
        entryclient_id = Entry(rate_menu_root, textvariable=client_id)
        entryclient_id.place(x=200, y=100, height=40, width=200)
        entryclient_rate = Entry(rate_menu_root, textvariable=client_rate)
        entryclient_rate.place(x=200, y=200, height=40, width=200)

        # 确认以及退出按钮
        def Button_Ok():
            # 注意数据类型转换
            db, cur = Sql_link()
            client_id = str(entryclient_id.get())
            client_rate = eval(entryclient_rate.get())
            try:
                sql = "UPDATE client SET rate = %d WHERE id = '%s'" % (client_rate,client_id)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo(message="积分修改!")
            except:
                messagebox.showerror(message="积分修改失败")

        Ok_Button = Button(rate_menu_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
        Exit_Button = Button(rate_menu_root, text="退出", font=("微软雅黑 -20"), command=rate_menu_root.destroy)
        Ok_Button.place(x=75, y=400, height=40, width=200)
        Exit_Button.place(x=325, y=400, height=40, width=200)
    # 功能菜单
    def manager_menu(self):
        # 创建窗口
        show_manager_root = Tk()
        show_manager_root.title("功能菜单")
        show_manager_root.config(width=600)
        show_manager_root.config(height=600)
        # 设置按钮
        button_manager1 = Button(show_manager_root, text="书籍管理", font=("微软雅黑 -20"), command=self.book_menu)
        button_manager2 = Button(show_manager_root, text="创建用户", font=("微软雅黑 -20"), command=self.create_client)
        button_manager3 = Button(show_manager_root, text="修改用户信息", font=("微软雅黑 -20"), command=self.edit_client)
        button_manager4 = Button(show_manager_root, text="积分信息", font=("微软雅黑 -20"), command=self.rate_menu)
        button_manager1.place(x=200, y=30, height=40, width=200)
        button_manager2.place(x=200, y=130, height=40, width=200)
        button_manager3.place(x=200, y=230, height=40, width=200)
        button_manager4.place(x=200, y=330, height=40, width=200)

        Exit_Button = Button(show_manager_root, text="退出", font=("微软雅黑 -20"), command=show_manager_root.destroy)
        Exit_Button.place(x=200, y=430, height=40, width=200)
    # 管理员登录
    def load_manager(self):
        # 创建窗口
        load_manager_root = Tk()
        load_manager_root.title("管理员用户登录")
        load_manager_root.config(width=600)
        load_manager_root.config(height=600)
        # 定义关联变量
        manager_name = StringVar(load_manager_root, value='')
        manager_code = StringVar(load_manager_root, value='')
        # 提示性标签
        labelmanager_name = Label(load_manager_root, text="管理员ID", font=("微软雅黑 -20"))
        labelmanager_code = Label(load_manager_root, text="管理员密码", font=("微软雅黑 -20"))
        # 设定标签位置
        labelmanager_name.place(x=200, y=100, height=40, width=200)
        labelmanager_code.place(x=200, y=200, height=40, width=200)
        # 定义录入信息文本框,以关联变量形式存储
        entrymanager_name = Entry((load_manager_root), textvariable=manager_name)
        entrymanager_name.place(x=200, y=150, height=40, width=200)
        entrymanager_code = Entry((load_manager_root), textvariable=manager_code)
        entrymanager_code.place(x=200, y=250, height=40, width=200)

        def Button_Ok():
            # 连接数据库
            db, cur = Sql_link()
            # 将得到的StringVar对象传值回来
            data_manager_name = str(entrymanager_name.get())
            data_manager_code = str(entrymanager_code.get())
            # 判断ID与密码是否能够匹配上
            sql = "SELECT * FROM manager WHERE id=%s AND code='%s'" % (data_manager_name, data_manager_code)
            search = cur.execute(sql)
            if (search > 0):
                messagebox.showinfo(title="恭喜", message="登录成功!!!")
                load_manager_root.destroy()
                self.manager_menu()
            else:
                messagebox.showerror(message="该账号不存在！")

        Ok_Button = Button(load_manager_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
        Exit_Button = Button(load_manager_root, text="退出", font=("微软雅黑 -20"), command=load_manager_root.destroy)
        Ok_Button.place(x=75, y=350, height=40, width=200)
        Exit_Button.place(x=325, y=350, height=40, width=200)
class Root_Manager(Manager):
    # 创建管理员
    def create_manager(self):
        # 创建窗口
        create_manager_root = Tk()
        create_manager_root.title("管理员用户创建")
        create_manager_root.config(width=600)
        create_manager_root.config(height=600)
        # 定义关联变量
        manager_name = StringVar(create_manager_root, value='')
        manager_code = StringVar(create_manager_root, value='')
        # 提示性标签
        labelmanager_name = Label(create_manager_root, text="管理员ID注册", font=("微软雅黑 -20"))
        labelmanager_code = Label(create_manager_root, text="管理员密码设置", font=("微软雅黑 -20"))
        # 设定标签位置
        labelmanager_name.place(x=200, y=100, height=40, width=200)
        labelmanager_code.place(x=200, y=200, height=40, width=200)
        # 定义录入信息文本框,以关联变量形式存储
        entrymanager_name = Entry((create_manager_root), textvariable=manager_name)
        entrymanager_name.place(x=200, y=150, height=40, width=200)
        entrymanager_code = Entry((create_manager_root), textvariable=manager_code)
        entrymanager_code.place(x=200, y=250, height=40, width=200)

        # 录入信息回调函数
        def Button_Ok():
            # 设置标志位判断是否存在ID重复
            flag = 0
            # 连接数据库
            db, cur = Sql_link()
            # 将得到的StringVar对象传值回来
            data_manager_name = str(entrymanager_name.get())
            data_manager_code = str(entrymanager_code.get())
            # 判断是否ID重复
            search = cur.execute("SELECT * FROM manager WHERE id =  '%s'" %(data_manager_name))
            if (search > 0):
                flag = 1
            else:
                flag = 0
            if (flag == 0):
                try:
                    # 写入数据
                    sql1 = "INSERT INTO manager(id,code)"
                    sql1 += "VALUES('%s','%s')" % (data_manager_name, data_manager_code)
                    cur.execute(sql1)
                    db.commit()
                    messagebox.showinfo(title="恭喜", message="注册成功！！！")
                    create_manager_root.destroy()
                except:
                    messagebox.showerror(message="注册失败！！！")
            else:
                messagebox.showerror("该用户名已注册！！！",message="注册失败！！！")

        # 确认以及退出按钮
        Ok_Button = Button(create_manager_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
        Exit_Button = Button(create_manager_root, text="退出", font=("微软雅黑 -20"), command=create_manager_root.destroy)
        Ok_Button.place(x=75, y=350, height=40, width=200)
        Exit_Button.place(x=325, y=350, height=40, width=200)
    # 展示管理员信息
    def show_manager_info(self):
        show_manager_info_root = Tk()
        show_manager_info_root.title("管理员信息")
        show_manager_info_root.config(width=600)
        show_manager_info_root.config(height=600)
        # 创建树对象用于展示数据
        show_manager_info_tree = ttk.Treeview(show_manager_info_root, height=30, columns=['1', '2'],
                                        show='tree headings')
        show_manager_info_tree.column('1', width=100, anchor='center')
        show_manager_info_tree.column('2', width=100, anchor='center')
        # 设置树的表头
        show_manager_info_tree.heading('1', text='ID')
        show_manager_info_tree.heading('2', text='CODE')
        try:
            db, cur = Sql_link()
            sql = "SELECT * FROM manager ORDER BY id DESC"
            cur.execute(sql)
            db.commit()
            # 给树各项参数赋值，若为NONE值则break
            for i in range(0, 30):
                results = cur.fetchone()
                while (results):
                    show_manager_info_tree.insert('', i, values=results)
                    break
        except:
            messagebox.showerror(message="排序失败!")
        show_manager_info_tree.pack()

        Exit_Button = Button(show_manager_info_root, text="退出", font=("微软雅黑 -20"), command=show_manager_info_root.destroy)
        Exit_Button.place(x=100, y=530, height=40, width=200)
    # 删除管理员
    def delete_manager(self):
        # 创建窗口
        delete_manager_root = Tk()
        delete_manager_root.title("管理员信息删除")
        delete_manager_root.config(width=600)
        delete_manager_root.config(height=600)

        manager_name = StringVar(delete_manager_root, value='')
        # 提示性标签
        labelmanager_name = Label(delete_manager_root, text="要删除的管理员ID", font=("微软雅黑 -20"))
        entrymanager_name = Entry(delete_manager_root, textvariable=manager_name)

        labelmanager_name.place(x=200, y=100, height=40, width=200)
        entrymanager_name.place(x=200, y=200, height=40, width=200)

        def Button_Ok():
            db, cur = Sql_link()
            manager_name = eval(entrymanager_name.get())
            # 查找对应的ID号
            sql = "SELECT * FROM manager WHERE id = %s" % (manager_name)
            search = cur.execute(sql)
            if (search > 0):
                messagebox.showinfo(message="删除成功!")
                # 删除目标行
                sql1 = "DELETE FROM manager WHERE id = %s" % (manager_name)
                cur.execute(sql1)
                db.commit()
            else:
                messagebox.showerror(message="该用户不存在!")

        Ok_Button = Button(delete_manager_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
        Exit_Button = Button(delete_manager_root, text="退出", font=("微软雅黑 -20"), command=delete_manager_root.destroy)
        Ok_Button.place(x=75, y=350, height=40, width=200)
        Exit_Button.place(x=325, y=350, height=40, width=200)
    # 超级管理员菜单
    def root_manager_menu(self):
        # 创建窗口
        show_root_manager_root = Tk()
        show_root_manager_root.title("功能菜单")
        show_root_manager_root.config(width=600)
        show_root_manager_root.config(height=600)
        # 设置按钮
        button_root_manager1 = Button(show_root_manager_root, text="创建管理员", font=("微软雅黑 -20"),
                                      command=self.create_manager)
        button_root_manager2 = Button(show_root_manager_root, text="管理员信息", font=("微软雅黑 -20"),
                                      command=self.show_manager_info)
        button_root_manager3 = Button(show_root_manager_root, text="管理员权限", font=("微软雅黑 -20"),
                                      command=self.manager_menu)
        button_root_manager4 = Button(show_root_manager_root, text="管理员删除", font=("微软雅黑 -20"),
                                      command=self.delete_manager)
        button_root_manager1.place(x=200, y=100, height=40, width=200)
        button_root_manager2.place(x=200, y=200, height=40, width=200)
        button_root_manager3.place(x=200, y=300, height=40, width=200)
        button_root_manager4.place(x=200, y=400, height=40, width=200)

        Exit_Button = Button(show_root_manager_root, text="退出", font=("微软雅黑 -20"), command=show_root_manager_root.destroy)
        Exit_Button.place(x=200, y=500, height=40, width=200)
    # 超级管理员登录
    def load_root_manager(self):
        # 创建窗口
        load_root_manager_root = Tk()
        load_root_manager_root.title("超级管理员用户登录")
        load_root_manager_root.config(width=600)
        load_root_manager_root.config(height=600)
        # 定义关联变量
        root_manager_name = StringVar(load_root_manager_root, value='')
        root_manager_code = StringVar(load_root_manager_root, value='')
        # 提示性标签
        labelroot_manager_name = Label(load_root_manager_root, text="超级管理员ID", font=("微软雅黑 -20"))
        labelroot_manager_code = Label(load_root_manager_root, text="超级管理员密码", font=("微软雅黑 -20"))
        # 设定标签位置
        labelroot_manager_name.place(x=200, y=100, height=40, width=200)
        labelroot_manager_code.place(x=200, y=200, height=40, width=200)
        # 定义录入信息文本框,以关联变量形式存储
        entryroot_manager_name = Entry((load_root_manager_root), textvariable=root_manager_name)
        entryroot_manager_name.place(x=200, y=150, height=40, width=200)
        entryroot_manager_code = Entry((load_root_manager_root), textvariable=root_manager_code)
        entryroot_manager_code.place(x=200, y=250, height=40, width=200)

        def Button_Ok():
            # 连接数据库
            db, cur = Sql_link()
            # 将得到的StringVar对象传值回来
            data_root_manager_name = str(entryroot_manager_name.get())
            data_root_manager_code = str(entryroot_manager_code.get())
            # 判断ID与密码是否能够匹配上
            sql = "SELECT * FROM root_manager WHERE id=%s AND code='%s'" % (data_root_manager_name, data_root_manager_code)
            search = cur.execute(sql)
            if (search > 0):
                messagebox.showinfo(title="恭喜", message="登录成功!!!")
                load_root_manager_root.destroy()
                self.root_manager_menu()
            else:
                messagebox.showerror(message="该账号不存在！")

        Ok_Button = Button(load_root_manager_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
        Exit_Button = Button(load_root_manager_root, text="退出", font=("微软雅黑 -20"), command=load_root_manager_root.destroy)
        Ok_Button.place(x=75, y=350, height=40, width=200)
        Exit_Button.place(x=325, y=350, height=40, width=200)
class Client(Manager):
    # 定义用户的ID和积分全局变量
    data_client_name = 0
    data_client_rate = 0
    # 用户登录
    def load_client(self):
        # 创建窗口
        load_client_root = Tk()
        load_client_root.title("用户登录")
        load_client_root.config(width=600)
        load_client_root.config(height=600)
        # 定义关联变量
        client_name = StringVar(load_client_root, value='')
        client_code = StringVar(load_client_root, value='')
        # 提示性标签
        labelclient_name = Label(load_client_root, text="用户ID", font=("微软雅黑 -20"))
        labelclient_code = Label(load_client_root, text="用户密码", font=("微软雅黑 -20"))
        # 设定标签位置
        labelclient_name.place(x=200, y=100, height=40, width=200)
        labelclient_code.place(x=200, y=200, height=40, width=200)
        # 定义录入信息文本框,以关联变量形式存储
        entryclient_name = Entry((load_client_root), textvariable=client_name)
        entryclient_name.place(x=200, y=150, height=40, width=200)
        entryclient_code = Entry((load_client_root), textvariable=client_code)
        entryclient_code.place(x=200, y=250, height=40, width=200)
        def Button_Ok():
            # 连接数据库
            db, cur = Sql_link()
            # 将得到的StringVar对象传值回来
            global data_client_name
            global data_client_rate
            data_client_name = str(entryclient_name.get())
            data_client_code = str(entryclient_code.get())
            # 判断ID与密码是否能够匹配上
            sql = "SELECT * FROM client WHERE id=%s AND code='%s'" % (
            data_client_name, data_client_code)
            search = cur.execute(sql)
            data = cur.fetchone()
            data_client_rate = data[2]
            if (search > 0):
                messagebox.showinfo(title="恭喜", message="登录成功!!! 积分数为%d " % (data[2]))
                load_client_root.destroy()
                self.client_menu()
            else:
                messagebox.showerror(message="该账号不存在！")

        Ok_Button = Button(load_client_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
        Exit_Button = Button(load_client_root, text="退出", font=("微软雅黑 -20"),
                             command=load_client_root.destroy)
        Ok_Button.place(x=75, y=350, height=40, width=200)
        Exit_Button.place(x=325, y=350, height=40, width=200)
    # 用户借书
    def client_borrow_book(self):
        global data_client_rate
        if data_client_rate > 0:

            # 创建窗口
            client_borrow_book_root = Tk()
            client_borrow_book_root.title("借出书籍")
            client_borrow_book_root.config(width=600)
            client_borrow_book_root.config(height=600)
            # 定义关联变量
            borrow_book_name = StringVar(client_borrow_book_root, value='')
            borrow_book_author = StringVar(client_borrow_book_root, value='')
            # 提示性标签
            labelborrow_book_name = Label(client_borrow_book_root, text="书籍名称", font=("微软雅黑 -20"))
            labelborrow_book_author = Label(client_borrow_book_root, text="书籍作者", font=("微软雅黑 -20"))
            # 设定标签位置
            labelborrow_book_name.place(x=200, y=100, height=40, width=200)
            labelborrow_book_author.place(x=200, y=200, height=40, width=200)
            # 定义录入信息文本框,以关联变量形式存储
            entryborrow_book_name = Entry((client_borrow_book_root), textvariable=borrow_book_name)
            entryborrow_book_name.place(x=200, y=150, height=40, width=200)
            entryborrow_book_author = Entry((client_borrow_book_root), textvariable=borrow_book_author)
            entryborrow_book_author.place(x=200, y=250, height=40, width=200)

            def Button_Ok():
                # 连接数据库
                db, cur = Sql_link()
                # 将得到的StringVar对象传值回来
                data_borrow_book_name = str(entryborrow_book_name.get())
                data_borrow_book_author = str(entryborrow_book_author.get())
                # 判断书籍信息是否正确
                sql = "SELECT * FROM book WHERE name='%s' AND author='%s'" % (data_borrow_book_name, data_borrow_book_author)
                search = cur.execute(sql)
                data = cur.fetchone()
                data_book_storge = data[5]
                if data_book_storge>0:
                    if (search > 0):
                        # 书籍库存-1
                        sql2 = "UPDATE book SET storge = storge - 1 WHERE name = '%s'AND author='%s'" % (
                            data_borrow_book_name, data_borrow_book_author)
                        global data_client_name
                        # 用户积分-1
                        sql3 = "UPDATE client SET rate = rate - 1 WHERE id = '%s'" % (data_client_name)
                        cur.execute(sql3)
                        cur.execute(sql2)
                        db.commit()
                        messagebox.showinfo(title="恭喜", message="借出成功!!!")
                        client_borrow_book_root.destroy()
                    else:
                        messagebox.showerror(message="该书籍不存在,请检查输入是否错误!")
                else:
                    sql4 = "UPDATE book SET state = '暂无' WHERE name = '%s'AND author='%s'" % (
                        data_borrow_book_name, data_borrow_book_author)
                    cur.execute(sql4)
                    db.commit()
                    messagebox.showinfo(title="抱歉", message="此书暂无库存!!!")

            Ok_Button = Button(client_borrow_book_root, text="确认", font=("微软雅黑 -20"), command=Button_Ok)
            Exit_Button = Button(client_borrow_book_root, text="退出", font=("微软雅黑 -20"), command=client_borrow_book_root.destroy)
            Ok_Button.place(x=75, y=350, height=40, width=200)
            Exit_Button.place(x=325, y=350, height=40, width=200)
        else:
            messagebox.showerror(message="积分数小于0,无法借书!")
    # 用户赠书
    def client_give_book(self):
        Manager.insert_book(self)
        global data_client_name
        db2, cur2 = Sql_link()
        sql2 = "UPDATE client SET rate = rate + 2 WHERE id = '%s'" % (data_client_name)
        cur2.execute(sql2)
        db2.commit()
    # 用户菜单
    def client_menu(self):
        # 创建窗口
        client_menu_root = Tk()
        client_menu_root.title("功能菜单")
        client_menu_root.config(width=600)
        client_menu_root.config(height=600)
        # 设置按钮
        button_client1 = Button(client_menu_root, text="借出书籍(积分-1)", font=("微软雅黑 -20"),
                                      command=self.client_borrow_book)
        button_client2 = Button(client_menu_root, text="按作者选书", font=("微软雅黑 -20"),
                                      command=self.sort_by_author)
        button_client3 = Button(client_menu_root, text="按类型选书", font=("微软雅黑 -20"),
                                      command=self.sort_by_type)
        button_client4 = Button(client_menu_root, text="赠与书籍(积分+2)", font=("微软雅黑 -20"),
                                      command=self.client_give_book)
        button_client1.place(x=200, y=50, height=40, width=200)
        button_client2.place(x=200, y=150, height=40, width=200)
        button_client3.place(x=200, y=250, height=40, width=200)
        button_client4.place(x=200, y=350, height=40, width=200)

        Exit_Button = Button(client_menu_root, text="退出", font=("微软雅黑 -20"),
                             command=client_menu_root.destroy)
        Exit_Button.place(x=200, y=450, height=40, width=200)

#生成类的实例
Manager_Object = Manager
Root_Manager_Object = Root_Manager
Client_Object = Client
#设置登录界面
root = Tk()
# 禁止最大化按钮（只显示最小化按钮和关闭按钮）
root.resizable(False,False)
root.minsize(600,600) # 最小尺寸
root.maxsize(600,600) # 最大尺寸
root.title("图书共享管理系统")

main_button1=Button(root,text="超级管理员登录",font=("微软雅黑 -20"),command=Root_Manager().load_root_manager)
main_button2=Button(root,text="管理员登录",font=("微软雅黑 -20"),command=Manager_Object().load_manager)
main_button3=Button(root,text="用户登录",font=("微软雅黑 -20"),command=Client_Object().load_client)
main_button1.place(x=200,y=100,height=40,width=200)
main_button2.place(x=200,y=200,height=40,width=200)
main_button3.place(x=200,y=300,height=40,width=200)

Exit_Button = Button(root, text="退出", font=("微软雅黑 -20"), command=root.destroy)
Exit_Button.place(x=200, y=400, height=40, width=200)
root.mainloop()
