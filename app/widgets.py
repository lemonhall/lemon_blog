from flask_appbuilder.widgets import ShowBlockWidget,FormWidget

class NoteShowWidget(ShowBlockWidget):
    template = 'widgets/note_show.html'

class NoteFormWidget(FormWidget):
    template = 'widgets/note_form.html'
