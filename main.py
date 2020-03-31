import json
import traceback

import grpc
from flask import Flask, request, jsonify
from google.protobuf.json_format import MessageToDict
from grpc._channel import _Rendezvous

from pb.recommand import recommand_pb2, recommand_pb2_grpc

app = Flask(__name__)


@app.route('/recommand', methods=['GET'])
def recommand():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = recommand_pb2_grpc.RecommandServiceStub(channel)
        params = get_request_params()
        try:
            response = client.Recommand(
                recommand_pb2.RecommandRequest(user_id=params['userId'], page=int(params['page']),
                                               page_size=int(params['pageSize'])))
            return generate_response_by_grpc_response(response)
        except _Rendezvous as e:
            traceback.print_exc()
            return generate_response_by_grpc_response("", 1, str(e))


@app.route('/setDefaultRecommandItems', methods=['POST'])
def set_default_recommand_items():
    with grpc.insecure_channel('localhost:50051') as channel:
        client = recommand_pb2_grpc.RecommandServiceStub(channel)
        params = get_request_params()
        try:
            response = client.SetDefaultRecommandItems(
                recommand_pb2.SetDefaultRecommandItemsRequest(item_ids=params['itemIds']))
            return generate_response_by_grpc_response(response)
        except _Rendezvous as e:
            traceback.print_exc()
            return generate_response_by_grpc_response("", 1, str(e))


def get_request_params():
    if request.method == 'GET':
        params = request.args.to_dict()
    elif request.method == 'POST' and "application/json" in request.headers.get("Content-Type", type=str):
        params = json.loads(request.data)
    else:
        params = request.form
    return params


def generate_response_by_grpc_response(data, code=0, msg="ok"):
    return jsonify({
        'code': code,
        'msg': msg,
        'data': MessageToDict(data)
    })


if __name__ == '__main__':
    app.run("localhost", "8888")
