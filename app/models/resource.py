from app import db, app
from app.models.group import permission

class Resource(db.Model):
    __tablename__ = "resources"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    resource_name = db.Column(db.String)
    resource_description = db.Column(db.String, nullable=True)

    groups = db.relationship(
        'Group', secondary=permission, lazy='joined', back_populates='resources')

    def __init__(self, resource_name=None, resource_description=None):
        self.resource_name = resource_name
        self.resource_description = resource_description

    def serialize(self):
        return {
            "id": self.id,
            "name": self.resource_name
        }
