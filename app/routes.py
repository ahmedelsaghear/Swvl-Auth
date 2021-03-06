from flask import request, make_response, jsonify
from app import app, auth_service

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/resource', methods=['POST'])
def post_resource():
    data = request.get_json()
    resource_name = data.get("name")
    resource = auth_service.set_resource(name=resource_name)
    res = make_response(jsonify(resource.serialize()))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


@app.route('/resource/<int:resource_id>', methods=['GET'])
@app.cache.memoize(timeout=300)
def get_resource(resource_id):
    resource = auth_service.get_resource(id=resource_id)
    res = make_response(jsonify(resource.serialize()))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


@app.route('/resource', methods=['GET'])
@app.cache.memoize(timeout=300)
def get_resources():
    resources = auth_service.get_resources()

    serialized_resources = [resource.serialize() for resource in resources]

    res = make_response(jsonify({"count": len(resources), "items": serialized_resources}))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


@app.route('/group', methods=['POST'])
def post_group():
    data = request.get_json()
    group_name = data.get("name")
    group_description = data.get("description")
    group = auth_service.set_group(name=group_name, description=group_description)
    res = make_response(jsonify(group.serialize()))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


@app.route('/group/<int:group_id>', methods=['GET'])
@app.cache.memoize(timeout=300)
def get_group(group_id):
    group = auth_service.get_group(id=group_id)
    res = make_response(jsonify(group.serialize()))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


@app.route('/group', methods=['Get'])
@app.cache.memoize(timeout=300)
def get_groups():
    groups = auth_service.get_groups()
    serialized_groups = [group.serialize() for group in groups]

    res = make_response(jsonify({"count": len(groups), "items": serialized_groups}))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200

@app.route('/group/<int:group_id>/users', methods=['POST'])
def attach_user(group_id):
    data = request.get_json()
    users = [str(user.get("userId")) for user in data]
    is_found = auth_service.link_user_with_groub(users_list=users, groub_id=group_id)
    if is_found is False:
        return "group is not found", 400
    return '', 204


@app.route('/group/<int:group_id>/resources', methods=['GET'])
@app.cache.memoize(timeout=300)
def get_group_resources(group_id):
    print "not cached_____________"
    resources = auth_service.get_group_resources(groub_id=group_id)
    resources_id = [resource.serialize() for resource in resources]
    res = make_response(jsonify({"count": len(resources), "items": resources_id}))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200


@app.route('/group/<int:group_id>/users', methods=['GET'])
@app.cache.memoize(timeout=300)
def get_group_users(group_id):
    users = auth_service.get_group_users(groub_id=group_id)
    users_id = [{"userId": user.user_id} for user in users]
    res = make_response(jsonify({"count": len(users), "items": users_id}))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 200

@app.route('/group/<int:group_id>/authorize', methods=['POST'])
def auth_group(group_id):
    data = request.get_json()
    print type(data), data
    resources = [int(resource.get("resourceId")) for resource in data]
    res = auth_service.authorize_resources(resources_list=resources, groub_id=group_id)
    if res is False:
        return 'group is not found ', 400
    return '', 204


@app.route('/authorized', methods=['GET'])
def auth():
    user_id = request.args.get("userId")
    resource_name = request.args.get("resourceName")
    is_authorized = auth_service.auth(user_id=user_id, resource_name=resource_name)


    res = make_response(jsonify({"authorized": True}))
    res.headers['Access-Control-Allow-Origin'] = '*'

    if is_authorized is True:
        return res, 200

    res = make_response(jsonify({"authorized": False}))
    res.headers['Access-Control-Allow-Origin'] = '*'
    return res, 403
