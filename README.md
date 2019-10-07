# ASiteByDjango

python3.7 版本与 Django 结合，学习并实现最简单的blog。

1. 安装Django :
  
   已安装python ， 通过命令行 pip install Django 安装。
   安装成功后，在系统环境变量配置path路径中添加  django-admin.exe （如 ;D:\Program Files\Python37\Scripts\django-admin.exe）
   再在命令窗口，执行  $ django-admin ， 查看是否配置成功。
 
2. Django 基本命令:

  2.1 新建项目：
        django-admin startproject ASiteByDjango
        ( 也可以通过IDE pycharm 创建项目 )
  
  2.2 新建App :python manage.py startapp app_name
  
  2.2 查看项目更多命令：python3 manage.py blogsite
  
  2.3 启动项目：  python3 manage.py runserver （http://127.0.0.1:8000）
  
  2.4 model: 
    2.4.1 在 app blogsite 的 models.py 中创建对象Article：
        from django.db import models


        class Article(models.Model):
            title = models.CharField(max_length=32, default='Title')
            content = models.TextField(null=True)
            pub_time = models.DateTimeField(auto_now=True)

          # 设置页面的Article展示名称
          def __str__(self):
             return self.title
          
   2.4.2 将对象与数据库连接：
       
       执行命令 ： python manage.py makemigrations
                  python manage.py migrate
    
    执行完成后，blogsite 下文件夹 migrations 中，存在 0001_initial.py文件
     
    项目目录下生成db.sqlite3文件。可使用Navicate查看创建的对象
     
   2.5 Admin:
      
      创建超级管理员：  python manage.py createsuperuser
      并设置用户名和密码
      
      之后，通过  http://127.0.0.1:8000/admin 路径可查看 admin 管理台。
    
  2.6 Django 项目环境终端
        python manage.py shell
      
 3. 项目目录下的 settings.py  可 添加blogsite， 配置数据库， 国际化等。（设置管理台 中文展示： LANGUAGE_CODE = 'zh-hans' ）
   
 4. 项目目录下urls.py 与blogsite中创建的urls.py 通过 include()函数关联。
   
 5.  blogsite 中涉及 html 页面，可以创建templates文件夹存放。
  
 6. ASiteByDjango/urls.py ——> blogsite/urls.py ——>  blogsite/views.py ——> xxx.html  
      
      
      
      
      
