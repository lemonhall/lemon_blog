import os
from flask import render_template,request,jsonify
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db
from .models import Notes
from flask_appbuilder.widgets import (
    ListBlock, ListItem, ListLinkWidget, ListThumbnail, ShowBlockWidget
)
from .widgets import NoteShowWidget,NoteFormWidget
from flask_appbuilder.api import BaseApi, expose
from werkzeug.datastructures import ImmutableMultiDict
import string
import random

from flask import send_from_directory

@appbuilder.app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(appbuilder.app.root_path, '/static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""
class NotesView(ModelView):
    datamodel = SQLAInterface(Notes)
    list_widget = ListLinkWidget
    show_widget = NoteShowWidget
    edit_widget = NoteFormWidget
    add_widget  = NoteFormWidget
    #edit_template = 'my_edit.html'
    label_columns = {'title':'标题','created_on':'创建于','changed_on':'修改于','content':'内容'}
    list_columns = ['title','created_on','changed_on']
    edit_exclude_columns = ['created_by', 'created_on', 'changed_by', 'changed_on']
    add_exclude_columns = ['created_by', 'created_on', 'changed_by', 'changed_on']
    show_exclude_columns = ['created_by', 'created_on', 'changed_by', 'changed_on']
    search_exclude_columns= ['created_by', 'created_on', 'changed_by', 'changed_on']


"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

#https://flask.palletsprojects.com/en/2.1.x/patterns/fileuploads/
class UpLoadApi(BaseApi):
    @expose('/upload_image', methods=['POST', 'GET'])
    def upload_image(self):
        #https://tedboy.github.io/flask/generated/generated/werkzeug.ImmutableMultiDict.html
        data = request.files
        #https://tedboy.github.io/flask/generated/generated/werkzeug.FileStorage.html
        image = data.get("image")
        #image.filename就可以读到文件名了
        upload_dir = os.path.join(appbuilder.app.root_path,"static/uploads")
        os_save_name = os.path.join(upload_dir,image.filename)
        #解决直接粘贴或者任何文件名重复时候的返回问题的一个文件名
        new_file_name = ""
        if os.path.exists(os_save_name):
            #得到文件名和扩展名
            name , extension = os.path.splitext(image.filename)
            # printing lowercase
            letters = string.ascii_lowercase
            random_str = ''.join(random.choice(letters) for i in range(20))
            new_file_name = name + "_" + random_str + extension
            print(new_file_name)
            os_save_name = os.path.join(upload_dir,new_file_name)
            image.save(os_save_name)
        else:
            new_file_name=image.filename
            image.save(os_save_name)
        #https://riptutorial.com/flask/example/5831/return-a-json-response-from-flask-api
        res = {'errno':0,'data':{'url':"/static/uploads/"+new_file_name}}
        return jsonify(res)

db.create_all()
appbuilder.add_view(
    NotesView,
    "日记",
    icon = "fa-folder-open-o",
    category = "日记",
    category_icon = "fa-envelope"
)

appbuilder.add_api(UpLoadApi)