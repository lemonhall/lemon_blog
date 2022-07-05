from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from flask_appbuilder.models.mixins import AuditMixin

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Notes(AuditMixin, Model):
	id = Column(Integer, primary_key=True)
	title = Column(String(256))
	content = Column(Text)

	def __repr__(self):
		return self.title