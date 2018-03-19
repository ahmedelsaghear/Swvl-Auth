from app import db, app
from app.models.user import user_group

permission = db.Table("permission",
                            db.Column("group_id", db.Integer,
                                      db.ForeignKey("groups.id")),
                            db.Column("resource_id", db.Integer,
                                      db.ForeignKey("resources.id"))
                            )

class Group(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    group_name = db.Column(db.String, nullable=True)
    group_description = db.Column(db.String, nullable=True)


    # using cascade = delete introduce the ability to remove from tables that have relationships
    users = db.relationship(
        'User', secondary=user_group, cascade="save-update, merge, delete", lazy='joined', back_populates='groups')

    resources = db.relationship(
        'Resource', secondary=permission, cascade="save-update, merge, delete", lazy='joined', back_populates='groups')

    def __init__(self, group_name=None, group_description=None):
        self.group_name = group_name
        self.group_description = group_description

    def serialize(self):
        return {
            "id": self.id,
            "name": self.group_name,
            "group_description": self.group_description

        }
