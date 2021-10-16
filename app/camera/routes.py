from flask import Blueprint, request, jsonify, Response
from app.store_stock import cameras

camera_blueprint = Blueprint('camera', __name__, url_prefix='/api/v1/cameras')

@camera_blueprint.route("/", methods=['GET'])
def tvs():
    if request.method == 'GET':
        return jsonify(cameras)


@camera_blueprint.route("/<int:camera_id>", methods=['GET'])
def tvs_id(camera_id):
    if request.method == 'GET':
        if camera_id not in cameras:
            return Response(status=404)
        return jsonify(cameras[camera_id])
