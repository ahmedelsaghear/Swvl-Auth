from sqlalchemy import and_
from sqlalchemy.orm import joinedload
from app import db
from app.models import User, Group, Resource, user_group, permission


def set_resource(name=None, description=None):
    new_resource = Resource(resource_name=name, resource_description=description)
    db.session.add(new_resource)
    db.session.commit()
    return new_resource


def get_resource(id):
    resource = db.session.query(Resource).filter(Resource.id == id).first()
    return resource


def get_resources():
    resources = db.session.query(Resource).all()
    return resources


def set_group(name=None, description=None):
    new_group = Group(group_name=name, group_description=description)
    db.session.add(new_group)
    db.session.commit()
    return new_group


def get_group(id):
    group = db.session.query(Group).filter(Group.id == id).first()
    return group


def get_groups():
    groups = db.session.query(Group).all()
    return groups


def link_user_with_groub(users_list, groub_id):
    print users_list[1], type(users_list[1])
    group = db.session.query(Group).filter(Group.id == groub_id).first()
    if group is None:
        return False
    users = db.session.query(User).filter(User.user_id.in_(users_list)).all()
    for user in users:
        group.users.append(user)
    db.session.commit()
    return True


def get_group_users(groub_id):
    group = db.session.query(Group).options(joinedload('users')).filter(Group.id == groub_id).first()
    return group.users


def authorize_resources(resources_list, groub_id):
    group = db.session.query(Group).filter(Group.id == groub_id).first()
    if group is None:
        return False
    resources = db.session.query(Resource).filter(Resource.id.in_(resources_list)).all()
    for resource in resources:
        group.resources.append(resource)
    db.session.commit()
    return True


def get_group_resources(groub_id):
    group = db.session.query(Group).options(joinedload('resources')).filter(Group.id == groub_id).first()
    return group.resources


def auth(user_id, resource_name):
    print user_id, type(user_id)
    print resource_name, type(resource_name)
    user = db.session.query(User).options(joinedload('groups')).filter(User.user_id == user_id).first()
    print user.__dict__
    if user is None:
        return None
    groups = [group.id for group in user.groups]
    print groups
    resource = db.session.query(Resource).join(permission).filter(
        and_(permission.c.group_id.in_(groups),
             Resource.resource_name == resource_name)).first()
    if resource:
        return True
    return False
