from app import db, app

user_group = db.Table("user_group",
                            db.Column("user_id", db.String(24),
                                      db.ForeignKey("users.user_id")),
                            db.Column("group_id", db.Integer,
                                      db.ForeignKey("groups.id"))
                            )


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.String(24), primary_key=True)
    user_name = db.Column(db.String)

    # by this relationship groups that a user belong to can be listed
    groups = db.relationship(
        'Group', secondary=user_group, cascade="save-update, merge, delete", lazy='joined', back_populates='users')

    def __init__(self, user_name=None, user_id=None):
        self.user_id = user_id
        self.user_name = user_name
