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

    groups = db.relationship(
        'Group', secondary=user_group, lazy='joined', back_populates='users')

