from flask import Blueprint, request, jsonify, Response

from app.store_stock import televisions

tv_blueprint = Blueprint('television', __name__, url_prefix='/api/v1/televisions')


@tv_blueprint.route("/", methods=['GET'])
def tvs():
    if request.method == 'GET':
        return jsonify(televisions)


@tv_blueprint.route("/<int:tv_id>", methods=['GET'])
def tvs_id(tv_id):
    if request.method == 'GET':
        if tv_id not in televisions:
            return Response(status=404)
        return jsonify(televisions[tv_id])



