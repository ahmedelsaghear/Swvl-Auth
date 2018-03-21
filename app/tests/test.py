import unittest
import json
from app import app, db
from app.models import Resource, Group, User
from app.tests import DBTestCase
from flask import jsonify


class TestEndPoints(DBTestCase):
    def test_post_resource(self):
        with self.client:
            response = self.client.post("/resource", data=json.dumps({"name": "booking"}), headers={'Content-Type': 'application/json'})
            data = json.loads(response.data)
            resource = db.session.query(Resource).filter(Resource.id == data.get("id")).first()
            if resource is None:
                return False
            return self.assertEquals(resource.resource_name, "booking")

    def test_post_group(self):
        with self.client:
            response = self.client.post("/group", data=json.dumps({"name": "swvl"}), headers={'Content-Type': 'application/json'})
            data = json.loads(response.data)
            group = db.session.query(Group).filter(Group.id == data.get("id")).first()
            if group is None:
                return False
            return self.assertEquals(group.group_name, "swvl")

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
        resource = Resource(resource_name="plying")
        group = Group(group_name="tactful")
        db.session.add(resource)
        db.session.add(group)
        db.session.commit()
        print "resource_________", resource.__dict__, resource.id
        resource_id = resource.id
        group_id = group.id
        print group_id
        with self.client:
            response = self.client.post("/group/" + str(group_id) + "/authorize", data=json.dumps([{"resourceId": resource_id}]), headers={'Content-Type': 'application/json'})
            return self.assertEquals(response.status_code, 204)

    def test_auth(self):
        user = User(user_id=100, user_name="ahmed")
        db.session.add(user)
        db.session.commit()
        user_id = user.user_id

        group = Group(group_name="swvl")
        group.users.append(user)
        db.session.add(group)
        db.session.commit()

        resource = Resource(resource_name="booking")
        resource.groups.append(group)
        db.session.add(resource)
        db.session.commit()

        response = self.client.get("authorized?userId=" + str(user_id) + "&resourceName=booking")
        data = json.loads(response.data)

        return self.assertEquals(data.get("authorized"), True)

    def test_add_users_to_group(self):
        user = User(user_id=100, user_name="ahmed")
        db.session.add(user)
        db.session.commit()
        user_id = user.user_id

        group = Group(group_name="swvl")
        group.users.append(user)
        db.session.add(group)
        db.session.commit()
        group_id = group.id

        with self.client:
            response = self.client.post("/group/" + str(group_id) + "/users", data=json.dumps([{"userId": user_id}]), headers={'Content-Type': 'application/json'})
            return self.assertEquals(response.status_code, 204)
