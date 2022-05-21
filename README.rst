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

- 这是个啥？::

    这是我写给我自己的blog程序，慢慢写，越写越舒服

    1、增删改查已经实现好了；感谢F.A.B的快速开发框架
    2、edit和add的form视图控件也已经自定义成功了，主要是和wangEditor联动在一起，结束了

- TODO::

    1、图床和这个富文本编辑器要联动在一起，这个是刚需
    2、看能否支持show模式下正确现实代码
    3、看是否能支持直接copy粘贴图片，这样就很快
    4、生成个摘要，然后发到豆瓣日记里面去联动起来，这个是很后期的功能了