from flask import jsonify, request
from flask_pymongo import PyMongo
from flask_restful import (
    Resource,
)
from app import app

mongo = PyMongo(app)

class TodoResource(Resource):
    def get(self, id):
        todo = mongo.db.todos.find_one({"id": id}, {"_id": 0})
        if not todo:
            abort(404, message="Todo {} doesn't exist".format(id))
        return jsonify({"status": "ok", "data": tweet_info})


    def delete(self, id):
        mongo.db.todos.remove({'id': id})
        return {}, 204

class TodoListResource(Resource):
    def get(self):
        data = []
        cursor = mongo.db.todos.find({}, {"_id": 0, "updated_at": 0}).limit(10)
        for item in cursor:
            data.append(item)
        return jsonify({"response": data})


    def post(self):
        data = request.get_json()
        if not data:
            data = {"status": "error"}
            return jsonify(data)
        mongo.db.todos.insert(data)
        return {"status": "ok"}, 201
