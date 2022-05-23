Base Skeleton to start your application using Flask-AppBuilder
--------------------------------------------------------------

- Install it::

	pip install flask-appbuilder
	git clone https://github.com/dpgaspar/Flask-AppBuilder-Skeleton.git

- Run it::

    $ export FLASK_APP=app
    # Create an admin user
    $ flask fab create-admin
    # Run dev server
    $ flask run


That's it!!

- docker打包安装::

    1、docker create -it ubuntu:latest
    2、得到一个shell
    3、apt-get update
    4、apt-get -y install python3-pip
    5、apt-get -y install git
    6、git clone https://github.com/lemonhall/lemon_blog.git
    7、pip3 install -r requirements.txt
    8、apt upgrade
    9、以上就完成了容器的准备工作
    用容器来构造一个新的images
    10、docker ps -a 找到上述容器的id
    11、docker commit -m "dou_note_fab container" -a "lemonhall" 2ac4927ac2fb dou_note_fab:v1
    12、docker images
    13、拿到对应的镜像的id：dou_note_fab v1  4c3bd4b7fae3  7 seconds ago   592MB
    14、将刚才那个镜像打包好，记得到其它目录下面去：docker save -o dou_notes.tar dou_note_fab:v1
    15、copy文件到nas，这个镜像其实之后也可以作为所有FAB类项目的images
    16、然后就是用系统load镜像，新建容器，映射文件夹这些，最后在路由器上做好端口映射就能访问到了



- 这是个啥？::

    这是我写给我自己的blog程序，慢慢写，越写越舒服

    1、增删改查已经实现好了；感谢F.A.B的快速开发框架
    2、edit和add的form视图控件也已经自定义成功了，主要是和wangEditor联动在一起，结束了

- TODO::

    1、图床和这个富文本编辑器要联动在一起，这个是刚需
    2、看能否支持show模式下正确现实代码
    3、看是否能支持直接copy粘贴图片，这样就很快
    4、生成个摘要，然后发到豆瓣日记里面去联动起来，这个是很后期的功能了


- 打开Public的权限::

    1、需要在config.py里，反注释掉AUTH_ROLE_ADMIN = 'Admin'
    2、然后进入管理界面后，针对Public这个role，配置NotesView的试图为show