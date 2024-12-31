from flask import Blueprint, abort, jsonify, make_response, request
from database.config import db

from models.student import Student

example_blueprint = Blueprint("example_blueprint", __name__)


def custom_error(message, status_code):
    return make_response(jsonify(message), status_code)


# Get all records
@example_blueprint.route("/list", methods=["GET"])
def index():
    students = Student.query.all()

    if students is None:
        return custom_error({"code": 404, "error": "Resource not found"}, 404)

    return make_response(jsonify([student.to_dict() for student in students]), 200)


# Get record by id
@example_blueprint.route("/<int:id>", methods=["GET"])
def get_student(id):
    student = Student.query.get(id)

    if student is None:
        return custom_error({"code": 404, "error": "Resource not found"}, 404)

    return make_response(jsonify(student.to_dict()), 200)


# Create record
@example_blueprint.route("/", methods=["POST"])
def create_student():
    if not request.json:
        return custom_error({"code": 400, "error": "Resource not found"}, 400)

    student = Student(
        firstname=request.json.get("firstname"),
        lastname=request.json.get("lastname"),
        email=request.json.get("email"),
        age=request.json.get("age"),
        bio=request.json.get("bio"),
    )

    db.session.add(student)
    db.session.commit()

    return jsonify(student.to_dict()), 201


# Delete record
@example_blueprint.route("/<int:id>", methods=["DELETE"])
def get_student(id):
    student = Student.query.get(id)

    if student is None:
        return custom_error({"code": 404, "error": "Resource not found"}, 404)

    db.session.delete(student)
    db.session.commit()

    return jsonify({"delete": True})


@example_blueprint.route("/<int:id>", methods=["PUT"])
def update_student(id):
    if not request.json:
        return custom_error({"code": 400, "error": "Resource not found"}, 400)

    student = Student.query.get(id)

    if student is None:
        return custom_error({"code": 404, "error": "Resource not found"}, 404)

    student.firstname = request.json.get("firstname", student.firstname)
    student.lasname = request.json.get("lasname", student.lasname)
    student.email = request.json.get("email", student.email)
    student.age = request.json.get("age", student.age)
    student.bio = request.json.get("bio", student.bio)

    db.session.commit()
    return jsonify(student.to_json())
