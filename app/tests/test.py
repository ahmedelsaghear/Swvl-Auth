import unittest
import json
from app import app, db
from app.models import Resource, Group, User
from app.tests import DBTestCase
from flask import jsonify


class TestEndPoints(DBTestCase):
    def test_post_resource(self):
        response = self.client.post("/resource", data=jsonify({"name": "booking"}))
        data = json.loads(response.data)
        resource = db.session.query(Resource).filter(Resource.id == data.get("id")).first()
        if resource is None:
            return False
        return self.assertEquals(resource.resource_name, "booking")

    def test_post_group(self):
        response = self.client.post("/group", data=jsonify({"name": "swvl"}))
        data = json.loads(response.data)
        group = db.session.query(Group).filter(Group.id == data.get("id")).first()
        if group is None:
            return False
        return self.assertEquals(group.resource_name, "swvl")

    def test_get_groups(self):
        group = Group(group_name="swvl")
        db.session.add(group)
        db.session.commit()

        response = self.client.get("group")
        data = json.loads(response.data)
        return self.assertEquals(data.get("count"), 1)

    def test_get_resources(self):
        resource = Resource(resource_name="booking")
        db.session.add(resource)
        db.session.commit()

        response = self.client.get("resource")
        data = json.loads(response.data)
        return self.assertEquals(data.get("count"), 1)

    def test_auth_group(self):
        resource = Resource(resource_name="booking")
        group = Group(group_name="swvl")
        db.session.add(resource)
        db.session.add(group)
        resource_name = resource.resource_name
        group_id = group.id

        response = self.client.post("/group/resources/" + str(group_id), data=jsonify([{"resourceId": resource_name}]))
        return self.assertEquals(response.status_code, 204)
    def test_auth(self):
        user = User(user_name="ahmed")
        db.session.add(user)
        user_id = user.user_id
        db.session.commit()

        group = Group(group_name="swvl")
        group.users.append(user)
        db.session.add(group)
        db.session.commit()

        resource = Resource(resource_name="booking")
        resource.groups.append(group)
        db.session.add(resource)
        db.session.commit()

        response = self.client.post("authorized?userId=" + str(user_id) + "&resourceName=booking")
        data = json.loads(response.data)
        return self.assertEquals(data.get("authorized"), True)

