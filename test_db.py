from app import app
from flask_appbuilder.models.sqla.interface import SQLAInterface
from app import appbuilder, db
from app.models import Notes
import logging
log = logging.getLogger(__name__)

try:
    db.session.add(Notes(title="test", content="testtesttesttesttesttesttest",created_by_fk=1,changed_by_fk=1))
    db.session.commit()
except Exception as e:
    log.error("Notes creation error: %s", e)
    db.session.rollback()
    exit(1)
