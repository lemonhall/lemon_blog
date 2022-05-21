from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi

from . import appbuilder, db
from .models import Notes
from flask_appbuilder.widgets import (
    ListBlock, ListItem, ListLinkWidget, ListThumbnail, ShowBlockWidget
)
from .widgets import NoteShowWidget,NoteFormWidget

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


db.create_all()
appbuilder.add_view(
    NotesView,
    "日记",
    icon = "fa-folder-open-o",
    category = "日记",
    category_icon = "fa-envelope"
)