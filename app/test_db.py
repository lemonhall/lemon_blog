import logging
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder, db
from models import Notes

datamodel = SQLAInterface(Notes)

#note=Notes()
#note.title="test"
#note.content="<p>kjljljljjljjljjkljjl</p>"
#note.user.id = 1

#datamodel.add(note)